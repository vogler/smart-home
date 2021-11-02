#!/usr/bin/env python3
# Send commands to SwitchBot Bot and Curtain.
# Extended https://gist.github.com/mugifly/a29f34df7de8960d72245fcb124513c7

import sys
import binascii
from bluepy.btle import Peripheral

if len(sys.argv) != 3:
    print('[Usage] python %s ff:ff:ff:ff:ff:ff CMD' % sys.argv[0])
    print('CMD:')
    print('  bot:     on, off, press, hold (5s)')
    print('  curtain: open, close')
    print('\nYou can get the MAC address of a Switchbot using `sudo hcitool lescan`')
    quit(1)

mac = sys.argv[1].lower()
cmd = sys.argv[2].lower()

# switch-case/pattern matching only introduced in Python 3.10... https://pakstech.com/blog/python-switch-case/

# bot
# https://github.com/OpenWonderLabs/python-host/wiki/Bot-BLE-open-API#0x01-execute-an-action
if cmd == 'on':
    s = '570101'
elif cmd == 'off':
    s = '570102'
elif cmd == 'press':
    s = '570100'
elif cmd == 'hold':
    s = '5701030504' # byte 05 is pause in seconds

# curtain
# https://github.com/OpenWonderLabs/python-host/wiki/Curtain-BLE-open-API#0x45-curtain-setting-command
elif cmd == 'open':
    s = '570f450105ff00'
elif cmd == 'close':
    s = '570f450105ff64'
else:
    print('Unknown command', cmd)
    quit(1)

print('Connecting to', mac)
p = Peripheral(mac, 'random')
service = p.getServiceByUUID('cba20d00-224d-11e6-9fb8-0002a5d5c51b')
characteristic = service.getCharacteristics('cba20002-224d-11e6-9fb8-0002a5d5c51b')[0]
characteristic.write(binascii.a2b_hex(s))
p.disconnect()
print('Executed', cmd)
