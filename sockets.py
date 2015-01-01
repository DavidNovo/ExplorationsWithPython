__author__ = 'davidnovogrodsky_wrk'
import socket

# making a TCP connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# print out the connection information
print(s)

# act like a browser
# where to connect to
server = 'pythonprogramming.net'
port = 80

server_ip = socket.gethostbyname(server)
print(server_ip)

# make a http request
request = "GET / HTTP/1.1\nHOST: "+server+"\n\n"

# connect to server
s.connect((server,port))
# in python 3 we use strings, not byte strings
# so we need to encode the string before sending
s.send(request.encode())
# size of buffer
result = s.recv(4000)

print(result)