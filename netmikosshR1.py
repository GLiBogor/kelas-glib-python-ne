#!/usr/bin/env python

from netmiko import ConnectHandler

ios_r1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.205',
    'username': 'alan',
    'password': 'cisco',
}

net_connect = ConnectHandler(**ios_r1)

output = net_connect.send_command('show ip int br')
print output

config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print output