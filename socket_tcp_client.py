import socket

if __name__=='__main__':
    try:
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        sk.connect(('localhost', 5858))
        while True:
            sk.send('Hello server from nnhiep'.encode('utf-8'))
            data = sk.recv(1024).decode('utf-8')
            print(data)
        sk.close()
    except socket.error as err:
        print(err)