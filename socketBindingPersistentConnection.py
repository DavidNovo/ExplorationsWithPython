__author__ = 'davidnovogrodsky_wrk'

import socket
import sys
from _thread import *

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
print('waiting for a connection...')



# send information to the socket/server
def threaded_client(conn):
    #sned message on connection
    conn.send(str.encode('Welcome, type your info\n'))
    # keep the connection open
    while True:
        data = conn.recv(2048)
        reply='Server output:'+data.decode('utf-8')
        if not data:
            break
        conn.sendall(str.encode(reply))
    conn.close()

while True:
    conn, addr = s.accept()
    print('connected to:' +addr[0]+':'+str(addr[1]))
    start_new_thread(threaded_client,(conn,))
