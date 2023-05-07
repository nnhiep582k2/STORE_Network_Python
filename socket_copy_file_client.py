# BT9: Viết chương trình sao chép file
# Client

import socket

if __name__=='__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.connect(('localhost', 5858))
    with open('test_copy.txt', 'wb') as f:
        while True:
            data = sk.recv(1024)
            if not data:
                break
            f.write(data)
    f.close()
    sk.close()