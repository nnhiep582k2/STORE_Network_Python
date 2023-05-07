# BT9: Viết chương trình sao chép file
# Server

import socket

if __name__=='__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind(('localhost', 5858))
    sk.listen(5)
    while True:
        client_sk, client_addr = sk.accept()
        f = open('Topic.txt', 'rb')
        data = f.read(1024)
        while data:
            client_sk.send(data)
            print('Sent: ', repr(data))
            data = f.read(1024)
        f.close()
        client_sk.close()
    sk.close()