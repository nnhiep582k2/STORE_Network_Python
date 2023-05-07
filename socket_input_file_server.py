# BT8: Viết chương trình gửi nhận cho nhập tên file
# Server

import socket

if __name__=='__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 9050
    sk.bind((host, port))
    sk.listen(5)
    while True:
        client_sk, client_addr = sk.accept()
        data = client_sk.recv(1024)
        if not data:
            break
        file_name = data.decode('utf-8')
        try:
            f = open(file_name + '.txt', 'rb')
            res = f.read()
            client_sk.send(res)
        except:
            print('Not found')
    f.close()
    client_sk.close()
    sk.close()