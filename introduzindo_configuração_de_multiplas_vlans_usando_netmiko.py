#!/usr/bin/python3

from netmiko import ConnectHandler 
import time

SW2 = {
    'device_type': 'cisco_ios',
	'ip': '192.168.122.222',
	'username': 'cisco',
	'password': 'cisco',
	'port': '22',
	'verbose': False,
	}

net_connect = ConnectHandler(**SW2)
print('Connected')

output = net_connect.send_command('show ip int brief')
print(output)
time.sleep(0.5)


for n in range(31, 61):
    print('Creating VLAN ' + str(n))
    config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
	output = net_connect.send_config_set(config_commands)
    print(output)

net_connect.send_command('wr')
time.sleep(0.5)

print("Configuration has been finished")  


	