#!/usr/bin/python
# coding=utf8
from scapy.all import sniff
from datetime import datetime
# from os import system
from sys import stdout
import paho.mqtt.client as mqtt

MQTT_BROKER = 'localhost'
MQTT_TOPIC = 'dash/' # + name of button; content will be datetime

client = mqtt.Client()
client.on_connect = lambda client, userdata, flags, rc: print(datetime.now(), "Connected to MQTT")
client.connect(MQTT_BROKER)
client.loop_start() # starts a thread

# blocked these macs in router to avoid notifications. however, this makes them try longer.
# fake server: https://github.com/ide/dash-button/issues/59
# maybe set google as primary dns and rpi as secondary: https://medium.com/@tombatossals/cheating-the-amazon-dash-iot-button-the-almost-easy-way-e5bc62f93f8c
macs = {
  "ac:63:be:ba:2f:85": "Dusche", # oral-b (Bad) battery empty (noticed 18.09.2019)
  "ac:63:be:ea:5b:1b": "Dusche", # kleenex (Bad) battery empty (noticed 15.09.2020)
  "00:fc:8b:d7:d5:3f": "Dusche", # finish (Bad) battery empty (noticed 08.05.2021)
  "18:74:2e:53:74:54": "Dusche", # nivea-men (Schrank)
  "68:37:e9:bc:f3:90": "Wäsche", # ariel (Schrank)
  "18:74:2e:3b:3c:09": "Rasur", # gillette (Bad)
  "18:74:2e:5b:57:ec": "Trakt", # nivea (Sofatisch)
  "b4:7c:9c:48:a3:01": "Bier", # heineken (Kühlschrank)
  "b4:7c:9c:e2:e8:5c": "Townew T1 Mülleimer Beutel gewechselt", # afri-cola (Küche)
  "00:fc:8b:9d:7c:da": "Zahnbürstenkopf", # swiffer (Schrank)
  "6c:56:97:8a:32:7a": "Tassimo", # tassimo (Bett)
  "fc:a6:67:c9:b0:1e": "Senseo",
  "18:74:2e:ad:44:11": "mentos"
}
cmds = {
  # "Licht (Küche)": "/home/pi/hs100.py toggle"
}

def udp_filter(p):
  # print(p.show())
  if p["IP"].id == 1:
    name = macs[p.src]
    # print(datetime.now(), name, p.summary())
    print(datetime.now(), name)
    stdout.flush()
    # if name in cmds:
    #   system(cmds[name])
    client.publish(MQTT_TOPIC + name, str(datetime.now()))

sniff(prn=udp_filter, filter="udp and port 67 and ether dst ff:ff:ff:ff:ff:ff", iface="eth0", store=0, lfilter=lambda x: x.src in macs)
# just had 'udp' as filter before, but that sometimes resulted in >60% CPU usage
# https://0xbharath.github.io/art-of-packet-crafting-with-scapy/scapy/sniffing/index.html
# 'Scapy sniffer is not designed to be super fast so it can miss packets sometimes. Always use use tcpdump when you can, which is more simpler and efficient.'
# sudo tcpdump -i eth0 -l -e -nn -vvv udp and port 67 and ether dst ff:ff:ff:ff:ff:ff
# -l     Make stdout line buffered.  Useful if you want to see the data while capturing it.
# -e     Print the link-level header on each dump line.  This can be used, for example, to print MAC layer addresses for protocols such as Ethernet and IEEE 802.11.
# -n     Don't convert addresses (i.e., host addresses, port numbers, etc.) to names.
# -vvv   Most verbose output with additional fields.
# port 67 is Bootstrap Protocol (BOOTP) DHCP server port for receiving client requests, 68 is client port for receiving server responses


# Notes on faster detection via extra wifi, firmware, AAA battery replacement:

# https://serverless.industries/2022/03/11/hack-the-dashbutton.html
# https://github.com/ridiculousfish/one-second-dash
# https://mpetroff.net/2016/07/new-amazon-dash-button-teardown-jk29lp/ teardown - I have rev02 with a AAA Duracell alkaline battery which is replaceable, but one has to pry open and damage the case
# https://kapuablog.wordpress.com/2018/03/18/amazon-dash-buttons-a-little-bit-of-iot/

# https://www.npmjs.com/package/homebridge-amazondash-mac
# 'By December 31, 2019, Amazon removed the capability to set up a Dash button for connection to a network. Also at that time, all Dash buttons that were connected to a network received an over-the-air update that disabled the button—a process Amazon refers to as "deregistration."'

# Programming rev01:
# https://github.com/dekuNukem/Amazon_Dash_Button components and pinouts for rev01
# https://learn.adafruit.com/dash-hacking-bare-metal-stm32-programming/overview
