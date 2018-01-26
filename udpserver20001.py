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
print('starting up on %s port %s' % server_address)
sock.bind(server_address)
counter = 0
print("server is on ")
first_bsm = True
previous_time = 1516197713264877
delta_time = 0
while True:
    data, address = sock.recvfrom(1000)
    timestamp = int(''.join(map(hex, data[1:9])).replace('0x', ''), 16)
    if timestamp > previous_time:
        delta_time=timestamp-previous_time
        previous_time = timestamp
        print(binascii.hexlify(data[0:36]))
        time_ = datetime.datetime.fromtimestamp(timestamp / 1000000.0)
        print("bsm time: ", time_, " delta_time in ms:  ", delta_time/1000.0, "src MAC: ", binascii.hexlify(data[28:34]))
