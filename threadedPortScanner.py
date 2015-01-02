__author__ = 'davidnovogrodsky_wrk'

# making a port scanner
__author__ = 'davidnovogrodsky_wrk'
import socket
import time
import threading
from queue import Queue

# the print command is not thread safe
# to prevent collisions use a lock
print_lock = threading.Lock()
target = 'pythonprogramming.net'


# define the port scanner function
def portscan(port):
    # making a TCP connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # try to make a connection
    # if there is a connection, print out port message
    try:
        con = s.connect((target,port))
        with print_lock:
            print('port ', port, 'is open')
        con.close()
    except:
        with print_lock:
            print('port ', port, 'is closed')

# define the threader that runs the port scan
def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

q = Queue()

# number of threads
# each thread contains a threader
for x in range(30):
    t = threading.Thread(target=threader)
    # make sure the work dies when thread ends
    t.daemon = True
    t.start()

# each worker is sent against a port
# this defines the number of ports to scan
for worker in range(1,101):
    q.put(worker)

q.join()

