#!/usr/bin/python3

from netmiko import ConnectHandler 
import time

SW3 = {
    'device_type': 'cisco_ios',
	'ip': '192.168.122.223',
	'username': 'cisco',
	'password': 'cisco',
	'port': '22',
	'verbose': False,
	}
SW4 = {
    'device_type': 'cisco_ios',
	'ip': '192.168.122.224',
	'username': 'cisco',
	'password': 'cisco',
	'port': '22',
	'verbose': False,
	}
    
all_devices = [SW3, SW4]

for device in all_devices:
    net_connect = ConnectHandler(**device)
    print('Connected')
    time.sleep(0.2)

    for n in range(2, 11):
        print('Creating VLAN ' + str(n))
        config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
	    output = net_connect.send_config_set(config_commands)
        print(output)
        
print("Configurations have been finished")  


	