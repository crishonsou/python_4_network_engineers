#!/usr/bin/python3

import getpass
import sys
import telnetlib

user = input("Enter your telnet username: ")  
password = getpass.getpass()

for n in range(200, 203):
    HOST = "192.168.255.{}\n".format(n).encode()

    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n") 
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
	

    tn.write(b"conf t\n")

	for n in range(2, 31):
	    tn.write("vlan {}\n".format(n).encode()) 
		tn.write("name Python_VLAN_{}\n".format(n).encode())

	tn.write(b"exit\n")
	tn.write(b"end\n")
    tn.write(b"wr\n")
	tn.write(b"exit\n") 

    print(tn.read_all().decode('ascii'))  