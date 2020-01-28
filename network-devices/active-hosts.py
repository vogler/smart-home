#!/usr/bin/env python3
# https://fritzconnection.readthedocs.io/en/1.2.1/sources/library.html#fritzhosts
# can also just run `fritzhosts -p <password> | grep active` to get the list

from fritzconnection.lib.fritzhosts import FritzHosts

import config

fh = FritzHosts(password=config.fritz_pwd)
hosts = fh.get_hosts_info()
for index, host in enumerate(hosts, start=1):
    status = 'active' if host['status'] else  '-'
    ip = host['ip'] if host['ip'] else '-'
    mac = host['mac'] if host['mac'] else '-'
    hn = host['name']
    # print(f'{index:>3}: {ip:<16} {hn:<28} {mac:<17}   {status}')
    if status == 'active':
        print(f'{index:>3}: {ip:<16} {hn:<28} {mac:<17}')
