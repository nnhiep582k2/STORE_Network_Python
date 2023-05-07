# BT3: Viết chương trình test client connect google

import socket, sys

if __name__=='__main__':
    try:
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print('Fail to create socket')
        print(str(e))
        sys.exit()
    print('Socket created')
    host = 'www.google.com'
    port = 80
    try:
        sk.connect((host, port))
    except socket.error as e:
        print('Fail to connect socket')
        print(str(e))
        sys.exit()
    while True:
        sk.send('GET / HTTP/1.0\r\n\r\n'.encode('utf-8'))
        data = sk.recv(1024)
        if not data:
            break
        print(data.decode('utf-8'))
    sk.close()