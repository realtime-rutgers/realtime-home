import socket
from threading import Thread


class My_Receive_Thread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.time = 0
        self.change = 1

    def run(self):
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ss.bind(('10.14.1.9', 8002))
        self.ss.listen(10)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("10.14.1.8", 8003))
        s.send(''.join(format(ord(i), '08b') + " " for i in "comnetsii").encode())
        s.close()

        while (True):
            self.sc, self.addr = self.ss.accept()
            self.l = self.sc.recv(1024).decode()
            print('message from server: ', self.l)


server = My_Receive_Thread()
server.start()
