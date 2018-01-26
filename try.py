import socket
import sys
import binascii
import datetime
import time
#
def hexint(b):
    return int(binascii.hexlify(b), 32)

#00 00 01 50 D3 F8 36 D8 
hexi=0x00000150D3F836D8
print(hexi)
#1446665272000

thisdate=datetime.datetime.fromtimestamp(hexi/1000.0)

print(thisdate)


nhexi=0x00000001abc2b1fb
print(nhexi)
nthisdate=datetime.datetime.fromtimestamp(nhexi/1000000.0)
print(nthisdate)

ts=1516197713264878

if(ts > 1516197713264877):
    nthisdate=datetime.datetime.fromtimestamp(ts/1000000.0)
    print(nthisdate)


# Create a TCP/IP socket
#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
#server_address = ('192.168.99.18', 20001)
#print ('starting up on %s port %s' % server_address)
#sock.bind(server_address)
#counter=0
#print("server is on ")

