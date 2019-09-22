import socket
import time
import hello


s = socket.socket()
host = socket.gethostname()
port = 9000
s.bind((host, port))  #Attatch socket
s.listen()

while True:
    c, addr = s.accept()
    print("Connection accepted from " + repr(addr[1]))
    c.send("Thank you for connecting")
    hello.bip()
    c.close()
    time.sleep(1)
