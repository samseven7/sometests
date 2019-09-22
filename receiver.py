import socket
import sys

s = socket.socket()
try:
    host = sys.argv[1]
except IndexError:
    print('Enter host IP address :')
    host = input()

port = 9000
s.connect((host, port))
m = s.recv(1024)
print(m)
s.close()
