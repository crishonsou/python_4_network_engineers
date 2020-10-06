#!/usr/bin/python3

import getpass
import sys
import telnetlib

HOST = "192.168.255.201"
user = input("Enter your telnet username: ")  
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n") 
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
	
vlan_name = "name Python_VLAN_"

tn.write(b"conf t\n")

for n in range(9, 30):
        tn.write("vlan {}\n".format(n).encode()) 
		tn.write("name Python_VLAN_{}\n".format(n).encode())

tn.write(b"exit\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii')) 