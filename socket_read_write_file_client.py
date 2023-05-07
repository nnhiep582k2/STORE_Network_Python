# BT7: Viết chương trình đọc ghi file
# Client

import socket

if __name__=='__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 9050
    sk.connect((host, port))
    f = open('attachment_received.pdf', 'wb')
    data = sk.recv(1024)
    while data:
        f.write(data)
        data= sk.recv(1024)
    f.close()
    sk.close()