import socket

s = socket.socket()
host = socket.gethostname()
port = 9000
s.connect((host, port))
m = s.recv(1024)
print(m)
s.close()
