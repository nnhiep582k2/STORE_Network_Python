import socket

if __name__=='__main__':
    try:
        sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)
        while True:
            sk.sendto('nnhiep from client'.encode('utf-8'), ('localhost', 5858))
            data, address = sk.recvfrom(1024)
            print(data.decode('utf-8'))
        sk.close()
    except socket.error as e:
        print(e)