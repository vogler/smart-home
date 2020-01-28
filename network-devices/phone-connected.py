#!/usr/bin/env python3
# faster to just check status of phone than all hosts

from fritzconnection.lib.fritzhosts import FritzHosts

import config

fh = FritzHosts(password=config.fritz_pwd)
he = fh.get_specific_host_entry(config.phone_mac)
print(he['NewActive'])
