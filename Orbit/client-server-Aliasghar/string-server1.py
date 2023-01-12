import socket
from threading import Thread

send_size = 1000


class My_Receive_Thread(Thread):
    def __init__(self):
        ''' Constructor. '''
        Thread.__init__(self)
        self.time = 0
        self.change = 1

    def run(self):
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ss.bind(('10.14.1.1', 8001))
        self.ss.listen(10)
        pp = 0
        a = ""
        while (True):
            self.sc, self.addr = self.ss.accept()
            self.l = self.sc.recv(send_size).decode()
            if self.l.__contains__("end"):
                nums = [float(a) for a in a.split(",")]
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.connect(("10.14.1.2", 8002))
                self.s.send(str(pp).encode())
                self.s.close()
            else:
                a += self.l
                pp += 1
                print("here", pp)


server = My_Receive_Thread()
server.start()
