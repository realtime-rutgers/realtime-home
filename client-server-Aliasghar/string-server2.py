import socket
from threading import Thread


class My_Receive_Thread(Thread):
    def __init__(self):
        ''' Constructor. '''
        Thread.__init__(self)
        self.time = 0
        self.change = 1

    def run(self):
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ss.bind(('10.14.1.8', 8003))
        self.ss.listen(10)
        while (True):
            self.sc, self.addr = self.ss.accept()
            self.l = self.sc.recv(1024).decode()
            self.l = self.l.replace(' ', "")
            print('message from client: ', self.l)
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect(("10.14.1.9", 8002))
            self.s.send(''.join(chr(int(self.l[i * 8:i * 8 + 8], 2)) for i in range(len(self.l) // 8)).encode())
            self.s.close()


server = My_Receive_Thread()
server.start()
