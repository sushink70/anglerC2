#server

import os
import socket
from _thread import *

def main():
    pass

class C2sever:
    def __init__(self):
        self.port = 31313
        self.serverLocalIP = '0.0.0.0'
        
    def threaded_client(connection):
        connection.send(str.encode('Welcome to the Servern'))
        while True:
            data = connection.recv(1024)
            reply = 'Server Says: ' + data.decode('utf-8')
            if not data:
                break
            connection.sendall(str.encode(reply))
        connection.close()

    def __socket (self):
        ThreadCount = 0 
        
        c2Sock = socket.socket()
        try:
            c2Sock.bind((self.serverLocalIP, self.port))
        except socket.error as e:
            print(str(e))
        print("Waiting for connections...")
        c2Sock.listen(100)

        while True:
            client, address = c2Sock.accept()
            print('Connected to: ' + address[0] + ':' + str(address[1]))
            start_new_thread(threaded_client, (client, ))
            ThreadCount += 1
            print('Thread Number: ' + str(ThreadCount))
        ServerSocket.close()
        
        
    def __get_session_id (self, var1):
        pass


if __name__ == '__main__':
    main()


connection.send(str.encode('Welcome to the Servern'))

malwareid.lst

TRGN-WIN
TRGN-LIN
TRGN-MAC
KYLG-WIN
KYLG-LIN
KYLG-MAC
