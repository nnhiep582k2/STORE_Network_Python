# BT2: Viết chương trình server đa luồng
# Server
import socket, sys
from _thread import *

def multi_thread_client(client_sk):
    client_sk.send('Hello client'.encode('utf-8'))
    while True:
        data = client_sk.recv(1024)
        if not data:
            break
        client_sk.sendall(data)
    client_sk.close()

if __name__=='__main__':
    try:
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print('Fail to create socket')
        print(str(e))
        sys.exit()
    print('Created socket')
    host = 'localhost'
    port = 6996
    ThreadCount = 0
    try:
        sk.bind((host, port))
    except socket.error as e:
        print('Fail to bind socket')
        print(str(e))
        sys.exit()
    sk.listen(5)
    print('Server is listening...')
    while True:
        client_sk, client_addr = sk.accept()
        start_new_thread(multi_thread_client, (client_sk, ))
        ThreadCount += 1
        print('Thread number: ' + str(ThreadCount))
    sk.close()