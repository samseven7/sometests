import socket
import time
import hello


s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = socket.gethostname()
port = 9000
s.bind((host, port))  #Attatch socket
s.listen()


c, addr = s.accept()
print("Connection accepted from " + repr(addr[1]))
c.sendall(b"Thank you for connecting")
hello.bip()
c.close()
time.sleep(1)

