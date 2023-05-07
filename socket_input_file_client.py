# BT9: Viết chương trình gửi nhận cho nhập tên file
# Client

import socket

if __name__=='__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 9050
    sk.connect((host, port))
    while True:
        data = input('Enter file name: ')
        sk.send(data.encode('utf-8'))
        temp = sk.recv(1024)
        print('Data from client: %s' % temp.decode('utf-8'))
    sk.close()