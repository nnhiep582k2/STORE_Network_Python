import socket

if __name__=='__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sk.connect(('localhost', 5858))
    data = sk.recv(1024).decode('utf-8')
    print(data)
    while True:
        sk.send('hello server'.encode('utf-8'))
        sk.send(input('Nhập a: ').encode('utf-8'))
        sk.send(input('Nhập b: ').encode('utf-8'))
        data = sk.recv(1024).decode('utf-8')
        print(data)