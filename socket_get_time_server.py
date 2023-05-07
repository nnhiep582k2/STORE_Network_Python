# BT10: Viết chương trình lấy thời gian
# Server

import socket
from datetime import datetime

if __name__=='__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind(('localhost', 5858))
    sk.listen(5)
    client_sk, client_addr = sk.accept()
    while True:
        data = client_sk.recv(1024).decode('utf-8')
        print(data)
        if not data or data == 'bye':
            client_sk.close()
            break
        elif data == 'getTime':
            time =  datetime.now()
            client_sk.send(str(time).encode('utf-8'))
        else:
            data = input('Enter message to client: ')
            client_sk.send(data.encode('utf-8'))
    sk.close()