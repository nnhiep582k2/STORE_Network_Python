# BT2: Viết chương trình server đa luồng
# Client
import socket, sys

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
    try:
        sk.connect((host, port))
    except socket.error as e:
        print('Fail to bind socket')
        print(str(e))
        sys.exit()
    while True:
        data = sk.recv(1024)
        if not data:
            break
        print(data.decode('utf-8'))
        sk.send('Hihihi server'.encode('utf-8'))    
    sk.close()