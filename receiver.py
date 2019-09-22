import socket

s = socket.socket()
host = socket.gethostname()
port = 9000
s.connect((host, port))
s.close()
