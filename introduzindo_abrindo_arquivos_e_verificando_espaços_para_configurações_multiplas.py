Por vezes, os IP´s dos switches não estão em ordem sequencial. Para resolver isso, vamos criar um arquivo e depois um programa para interagir
com esse arquivo, verificando quais os switches estão aptos para serem configurados:

myswitches.txt

192.168.255.200
192.168.255.201
192.168.255.202
192.168.255.203


nano testloop.py

f = open('myswitches.txt')
for line in f:
    print(line)
f.close()
   


#!/usr/bin/python3

import getpass
import sys
import telnetlib

user = input("Enter your telnet username: ")  
password = getpass.getpass()

f = open('myswitches.txt')

for line in f:
    print('Configuring Switch " + line)
    
    HOST = line

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