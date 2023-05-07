import socket

if __name__=='__main__':
    try:
        sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
        sk.bind(('localhost', 5858))
        while True:
            data, address = sk.recvfrom(1024)
            print(data.decode('utf-8'))
            sk.sendto('nnhiep from server'.encode('utf-8'), address)
        sk.close()
    except socket.error as err:
        print(err)