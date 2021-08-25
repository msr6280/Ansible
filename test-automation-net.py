#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

host = input("Enter your hostname: ")
device = { 
    'device_type': 'cisco_ios',
    'host': host,
    'username': 'pyclass',
    'password': getpass,
} 

net_connect = ConnectHandler(**device)
output = net_connect.send_command("show ip int brief")
print(output) 