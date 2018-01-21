#!/usr/bin/env python

import getpass
import sys
import telnetlib

user = raw_input("Enter your telnet username : ")
password = getpass.getpass()
f = open('pool-ip.txt')

for line in f:
    print ("Configure Router ") + (line)
    host = line

    tn = telnetlib.Telnet(host)

    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    tn.write("conf t\n")

    #perulangan
    for n in range(0,5):
        tn.write("int loop " + str(n) + "\n")
        tn.write("ip address 1.1.1." + str(n+1) + " 255.255.255.255" + "\n")


    tn.write("end\n")
    tn.write("exit\n")

    print tn.read_all()
