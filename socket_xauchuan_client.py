import socket

if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.connect(('127.0.0.1', 9050))
    data = sk.recv(1024)
    print(data.decode('utf-8'))
    data = 'hello server'
    sk.send(data.encode('utf-8'))
    while True:
        data = input('Nhap xau: ')
        if data == 'bye':
            sk.send(data.encode('utf-8'))
            break
        sk.send(data.encode('utf-8'))
        data = sk.recv(1024)
        print(data.decode('utf-8'))
    sk.close()