import socket


class Receiver:
    def __init__(self, host="192.168.1.28", port=9000, size=1024):
        self.port = port
        self.host = host
        self.size = size

    def run(self):
        s = socket.socket()
        s.connect((self.host, self.port))
        m = s.recv(self.size)
        print(m)
        s.close()


r = Receiver(size=128, host="192.168.1.28")
r.run()
