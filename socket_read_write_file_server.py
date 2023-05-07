# BT7: Viết chương trình đọc ghi file
# Server

import socket

if __name__=='__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 9050
    sk.bind((host, port))
    sk.listen(5)
    f = open('attachment.pdf', 'rb')
    data = f.read()
    client_sk, client_addr = sk.accept()
    while data:
        client_sk.send(data)
        data = f.read(1024)
    f.close()
    client_sk.close()
    sk.close()