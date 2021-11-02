#!/usr/bin/env python3
# Simplest Switchbot Command
# https://gist.github.com/mugifly/a29f34df7de8960d72245fcb124513c7
# Thanks to https://gist.github.com/aerialist/163a5794e95ccd28dc023161324009ed

import sys
import binascii
from bluepy.btle import Peripheral

if len(sys.argv) != 3:
    print('[Usage] python %s ff:ff:ff:ff:ff:ff MODE' % sys.argv[0])
    print('\nMODE: open/off, close/on')
    print('\nYou can get a MAC address of Switchbot, with using $ sudo hcitool lescan')
    quit(1)

mac = sys.argv[1]
mode = sys.argv[2]

print('Connecting... ' + mac)
p = Peripheral(mac, 'random')
service = p.getServiceByUUID('cba20d00-224d-11e6-9fb8-0002a5d5c51b')
hand = service.getCharacteristics('cba20002-224d-11e6-9fb8-0002a5d5c51b')[0]

if mode == 'open' or mode == 'off':
    hand.write(binascii.a2b_hex('570f450105ff00'))
elif mode == 'close' or mode == 'on':
    hand.write(binascii.a2b_hex('570f450105ff64'))

print(mode)
p.disconnect()
