# setup: sudo pip install bluepy paho-mqtt
# run: sudo python3 toothbrush2mqtt.py 04:EE:03:BB:77:88 rpi3 toothbrush

# adapted from https://github.com/rfaelens/domotica/blob/master/mqtt-toothbrush.py
# via https://github.com/vogler/toothbrush (fork, deprecated, not simple enough, too many deps, only every 10s?)
# see https://github.com/vogler/toothbrush/blob/master/notes.md

# Tried https://github.com/zewelor/bt-mqtt-gateway which also only reported every 10s and did not seem as stable.

# The BLE data is not as detailed as what the app shows:
# Position and orientation are missing, pressure value just changes if it is so high that the red LED turns on.
# The toothbrush is not publishing via BLE if it's connected in the Oral-B app! So this script only captures data when brushing without the app open.
# Could try to make a connection similar to the app to get detailed data without the app.

import sys
import bluepy.btle as btle
# TODO just pipe into mosquitto_pub?
import paho.mqtt.client as mqtt
mqttc=mqtt.Client()
import json
from datetime import datetime

if len(sys.argv) != 4:
    print("Usage: sudo python3", sys.argv[0], "mac-address mqtt-host mqtt-topic")
    exit(1)

address = sys.argv[1].lower()
host = sys.argv[2]
topic = sys.argv[3]
debug = False

# example:
# dc000471040232000000010004 {'running': 2, 'pressure': 50, 'time': 0, 'mode': 0, 'quadrant': 1, 'quadrant_percentage': 0} 0
# dc00047104033a000001010004 {'running': 3, 'pressure': 58, 'time': 0, 'mode': 1, 'quadrant': 1, 'quadrant_percentage': 0} 0
# dc000471040332000001010004 {'running': 3, 'pressure': 50, 'time': 0, 'mode': 1, 'quadrant': 1, 'quadrant_percentage': 0} 0
# dc000471040332000101010304 {'running': 3, 'pressure': 50, 'time': 1, 'mode': 1, 'quadrant': 1, 'quadrant_percentage': 3} 3
# dc000471040332000201010604 {'running': 3, 'pressure': 50, 'time': 2, 'mode': 1, 'quadrant': 1, 'quadrant_percentage': 6} 6
# dc000471040332000301010a04 {'running': 3, 'pressure': 50, 'time': 3, 'mode': 1, 'quadrant': 1, 'quadrant_percentage': 10} 10
# dc000471040332000401010d04 {'running': 3, 'pressure': 50, 'time': 4, 'mode': 1, 'quadrant': 1, 'quadrant_percentage': 13} 13
# dc00047104023a000400010d04 {'running': 2, 'pressure': 58, 'time': 4, 'mode': 0, 'quadrant': 1, 'quadrant_percentage': 13} 13
# dc000471040232000400010d04 {'running': 2, 'pressure': 50, 'time': 4, 'mode': 0, 'quadrant': 1, 'quadrant_percentage': 13} 13
# dc000471040432000000010d04 {'running': 4, 'pressure': 50, 'time': 0, 'mode': 0, 'quadrant': 1, 'quadrant_percentage': 13} 13

class ScanDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        # if isNewDev or isNewData: print(dev.addr, isNewDev, isNewData, dev.rssi, dev.updateCount, dev.getValueText(255))
        if dev.addr == address and (isNewDev or isNewData):
            s = dev.getValueText(255)
            b = bytes.fromhex(s) # len 13
            o = {
                    # b[0] to b[4] are constant 220 0 4 113 4
                    "running": b[5] == 3, # 2 = off, 3 = on, 4 = done?
                    "pressure": round((b[6]-50)/192*100), # 50 (fine) or 242 (red) while running
                    "time": b[7]*60 + b[8], # min + sec
                    "mode": b[9], # 0 off, [1,7,2,4,3,6] cycled from top to bottom, mode (icon):
                      # 1 Tägliche Reinigung
                      # 7 Pro-Clean (Zahn mit Plus)
                      # 2 Sensitiv (Feder)
                      # 4 Aufhellen (Diamant)
                      # 3 Zahnfleisch-Schutz (Wellen)
                      # 6 Zungenreinigung (Zunge)
                    # "quadrant": b[10], # just counted up every 30s, starts with 1
                    # "quadrant_percentage": b[11], # also just increases with time, even if not moving
                    # b[12] is constant 4
                }
            print(datetime.now(), list(b), o)
            mqttc.publish(topic, json.dumps(o))

            for adtype, description, value in dev.getScanData():
                if debug: print(dev.addr+": adtype='"+str(adtype)+"', descr='"+description+"', value='"+value+"'")
                # adtype='1', descr='Flags', value='06'
                # adtype='255', descr='Manufacturer', value='dc00047104023a002b00022b04'
                # adtype='2', descr='Incomplete 16b Services', value='0000fe0d-0000-1000-8000-00805f9b34fb'
                # value of 1 and 2 is constant, 255's changes

mqttc.connect(host)
mqttc.loop_start()

scanner = btle.Scanner().withDelegate(ScanDelegate())
scanner.start(passive=True)
while True:
        try:
            scanner.process()
        except btle.BTLEException as e:
            print('Problem with the Bluetooth adapter : {}'.format(e))
            scanner.clear()
            print('Retrying...')
            # scanner.stop()
            # scanner.clear()
            # scanner.start(passive=True)
