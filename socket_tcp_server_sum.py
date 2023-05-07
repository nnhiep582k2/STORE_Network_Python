import socket

if __name__=='__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sk.bind(('localhost', 5858))
    sk.listen(5)
    client_sk, client_addr = sk.accept()
    client_sk.send('hello client'.encode('utf-8'))
    while True:
        data = client_sk.recv(1024).decode('utf-8')
        print(data)
        num1 = client_sk.recv(1024).decode('utf-8')
        num2 = client_sk.recv(1024).decode('utf-8')
        sum = int(num1) + int(num2)
        print(str(sum))