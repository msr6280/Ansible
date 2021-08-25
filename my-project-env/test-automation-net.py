#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

host = input("Enter your hostname: ")
device = { 
    'device_type': 'cisco_nxos',
    'host': host,
    'username': "admin",
    'password': "admin",
} 

net_connect = ConnectHandler(**device)
output = net_connect.send_command("show  interface status | inc connected)")
output = net_connect.send_command("show  ip interface brief ")
output = net_connect.send_command("show  run")
print(output) 