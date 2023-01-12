import random
import socket
from threading import Thread
import struct

send_size = 1000


class My_Receive_Thread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.time = 0
        self.change = 1

    def run(self):
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ss.bind(('10.14.1.2', 8002))  # Ip and port of the current node
        self.ss.listen(10)
        values = []
        frm = ""
        for i in range(1, 10):
            frm += "b "
            values.append(i)
        frm = frm[:-1]
        packer = struct.Struct(frm)
        packed_data = packer.pack(*values)
        print(values, *values, packed_data)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("10.14.1.1", 8001))  # Ip and port of the other node
        s.send(packed_data)
        s.close()

        while True:
            self.sc, self.addr = self.ss.accept()
            self.l = self.sc.recv(1024).decode()
            print('message from server: ', self.l)


server = My_Receive_Thread()
server.start()
