import random
import socket
from threading import Thread

send_size=1000

class My_Receive_Thread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.time = 0
        self.change = 1

    def run(self):
        a = []
        for i in range(1000 * 1000):
            a.insert(i, str(i))
            # a.insert(i, str(random.random()))
        print(len(a))
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ss.bind(('10.14.1.2', 8002))
        self.ss.listen(10)
        tt = ",".join(a)
        while len(tt) > 0:
            r, tt = tt[:send_size], tt[send_size:]
            print("zzz", len(tt))
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("10.14.1.1", 8001))
            s.send(r.encode())
            s.close()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("10.10.1.1", 8001))
        s.send("end".encode())
        s.close()

        while True:
            self.sc, self.addr = self.ss.accept()
            self.l = self.sc.recv(1024).decode()
            print('message from server: ', self.l)
            print(" ")
            print(" ")
            print(" ")


server = My_Receive_Thread()
server.start()
