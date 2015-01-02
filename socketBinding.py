__author__ = 'davidnovogrodsky_wrk'

import socket
import sys

# TCP socket with IP address
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 5555

try:
    s.bind((host,port))
except socket.error as e:
    print(str(e))

# number of connections to allow
s.listen(5)
conn, addr = s.accept()
print('connected to:' +addr[0]+':'+str(addr[1]))



