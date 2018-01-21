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

net_connect = ConnectHandler(**ios_r1)
config_command_tunnel = ['int tunnel 123', 'ip address 123.123.123.1 255.255.255.252', 'tunnel source fa0/0', 'tunnel destination 192.168.122.221']
config_command_loopback = ['int lo0','ip address 5.5.5.5 255.255.255.0']
config_command_iegrp = ['router eigrp 1','network 123.123.123.0 0.0.0.3', 'network 5.5.5.5 0.0.0.255']
output_tunnel = net_connect.send_config_set(config_command_tunnel)
output_loopback = net_connect.send_config_set(config_command_loopback)
output_eigrp = net_connect.send_config_set(config_command_iegrp)
print output_tunnel,output_loopback,output_eigrp

net_connect = ConnectHandler(**ios_r2)
config_command_tunnel = ['int tunnel 123', 'ip address 123.123.123.2 255.255.255.252', 'tunnel source fa0/0', 'tunnel destination 192.168.122.205']
config_command_loopback = ['int lo0','ip address 6.6.6.6 255.255.255.0']
config_command_iegrp = ['router eigrp 1','network 123.123.123.0 0.0.0.3', 'network 6.6.6.6 0.0.0.255']
output_tunnel = net_connect.send_config_set(config_command_tunnel)
output_loopback = net_connect.send_config_set(config_command_loopback)
output_eigrp = net_connect.send_config_set(config_command_iegrp)
print output_tunnel,output_loopback,output_eigrp