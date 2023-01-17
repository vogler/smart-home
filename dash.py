#!/usr/bin/python
# coding=utf8
from scapy.all import sniff
from datetime import datetime
from os import system
from sys import stdout

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
    if name in cmds:
      system(cmds[name])

sniff(prn=udp_filter, filter="udp", iface="eth0", store=0, lfilter=lambda x: x.src in macs)
