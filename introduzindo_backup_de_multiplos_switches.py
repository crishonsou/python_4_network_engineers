#!/usr/bin/python3

import getpass
import telnetlib

## Ask For Username and Password
user = input("Enter your telnet username: ")  
password = getpass.getpass()

## Open a file called myswitches

f = open('myswitches.txt')

## Telnet to the switches and get running config
for line in f:
    print("Getting running config from Switch " + line) 
    
    HOST = line.strip()

    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n") 
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
	

    tn.write(b"terminal length 0\n")
    tn.write(b"show run\n")
	tn.write(b"exit\n") 
    
    readoutput = tn.read_all()
    saveoutput = open("switch" + HOST, "b+w")
    saveoutput.write(readoutput)
    saveoutput.write(b"\n")
    saveoutput.close()
        
    
    print(tn.read_all().decode('ascii'))  

