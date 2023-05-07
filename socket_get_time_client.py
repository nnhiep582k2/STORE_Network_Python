# BT10: Viết chương trình lấy thời gian
# Client

import socket

if __name__=='__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.connect(('localhost', 5858))
    while True:
        data = input('Enter message to server: ')
        sk.send(data.encode('utf-8'))
        if data == 'bye':
            sk.close()
            break
        data = sk.recv(1024)
        print(data.decode('utf-8'))