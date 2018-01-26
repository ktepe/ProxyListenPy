import socket
import sys
import binascii
import datetime
import time
#
def hexint(b):
    return int(binascii.hexlify(b), 32)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('192.168.99.18', 20001)
print ('starting up on %s port %s' % server_address)
sock.bind(server_address)
counter=0
print("server is on ")
while True:
    
    data, address = sock.recvfrom(1000)

    print(binascii.hexlify(data[0:32]))
    print(data[0:32])
    timestamp = int(''.join(map(hex, data[1:9])).replace('0x', ''), 16)
    value = datetime.datetime.fromtimestamp(timestamp)
    print(value, timestamp)
