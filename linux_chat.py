import socket
import threading
import os
import time
os.system(tput setaf 2)
os.system(figlet -f "CHAT APP!!")
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

os.system(tput setaf 3)
serverip = "your_ip"
serverport = 6036

clientip = input("\n\t\tEnter Your client IP :")
clientport = 6036

s.bind( (serverip,serverport) )

def send():
     while True:
            msg = input("Your Message : ").encode()
            s.sendto(msg,(clientip,clientport))
            if msg.decode() == "exit" or msg.decode() == "quit" or msg.decode() == "bye":
                os._exit(1)
os.system(tput setaf 6)
def recv():
     while True:
            msg = s.recvfrom(1024)
            if msg[0].decode() == "exit" or msg[0].decode() == "quit" or msg[0].decode() == "bye":
                os._exit(1)
            print('\n\t\t\t\t\t\tReceived Msg : '+msg[0].decode())
            time.sleep(5)

t1 = threading.Thread(target=recv)
t1.start()

t2 = threading.Thread(target=send)
t2.start()