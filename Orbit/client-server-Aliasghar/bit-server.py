import socket
from threading import Thread
import binascii
import struct
import sys

send_size = 1000
frm = ""
for i in range(1, 10):
    frm += "b "
frm = frm[:-1]
unpacker = struct.Struct(frm)


class My_Receive_Thread(Thread):
    def __init__(self):
        ''' Constructor. '''
        Thread.__init__(self)
        self.time = 0
        self.change = 1

    def run(self):
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ss.bind(('10.14.1.1', 8001))  # Ip and port of the current node
        self.ss.listen(10)
        pp = 0
        a = ""
        while (True):
            self.sc, self.addr = self.ss.accept()
            self.l = self.sc.recv(unpacker.size)

            print(sys.stderr, 'received ', binascii.hexlify(self.l))

            unpacked_data = unpacker.unpack(self.l)
            print(sys.stderr, 'unpacked:', unpacked_data)
            print("zzzz", unpacked_data)


server = My_Receive_Thread()
server.start()

