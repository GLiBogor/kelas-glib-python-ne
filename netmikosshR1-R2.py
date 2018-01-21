#!/usr/bin/env python

from netmiko import ConnectHandler

ios_r1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.205',
    'username': 'alan',
    'password': 'cisco',
}

ios_r2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.221',
    'username': 'alan',
    'password': 'cisco',
}

all_device = [ios_r1, ios_r2]

for devices in all_device:
    net_connect = ConnectHandler(**devices)
    config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
    output = net_connect.send_config_set(config_commands)
    print output