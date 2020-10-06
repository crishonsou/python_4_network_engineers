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

tn.write(b"conf t\n")
tn.write(b"vlan 2\n")
tn.write(b"name Python_VLAN2\n")
tn.write(b"exit\n")
tn.write(b"vlan 3\n")
tn.write(b"name Python_VLAN3\n")
tn.write(b"exit\n")
tn.write(b"vlan 4\n")
tn.write(b"name Python_VLAN4\n")
tn.write(b"exit\n")
tn.write(b"vlan 5\n")
tn.write(b"name Python_VLAN5\n")
tn.write(b"exit\n")
tn.write(b"vlan 6\n")
tn.write(b"name Python_VLAN6\n")
tn.write(b"exit\n")
tn.write(b"vlan 7\n")
tn.write(b"name Python_VLAN7\n")
tn.write(b"exit\n")
tn.write(b"vlan 8\n")
tn.write(b"name Python_VLAN8\n")
tn.write(b"exit\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))