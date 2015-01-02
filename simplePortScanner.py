__author__ = 'davidnovogrodsky_wrk'

# making a port scanner
__author__ = 'davidnovogrodsky_wrk'
import socket
import time

# making a TCP connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server = 'pythonprogramming.net'
server = 'google.com'

# def the method for scanning a port
def pscan(port):
    try:
        # connect to server
        s.connect((server,port))
        return True
    except:
        return False

startTime = time.time()
for x in range(1,100):
    if pscan(x):
        print('Port ', x,' is open')
    else:
        print('Port ',x,' is closed')
endTime = time.time()

# how ling did the scan take?
print( 'The scan took: ' ,endTime-startTime)