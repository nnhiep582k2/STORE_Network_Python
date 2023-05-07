import socket

if __name__=='__main__':
    try:
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        sk.bind(('localhost', 5858))
        sk.listen(5)
        while True:
            client_sk, client_addr = sk.accept()
            data = client_sk.recv(1023).decode('utf-8')
            print(data)
            client_sk.send('nnhiep nè'.encode('utf-8'))
        sk.close()
    except socket.error as err:
        print(err)
    