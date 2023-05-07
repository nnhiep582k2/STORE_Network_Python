import socket
import threading
import random

host = 'localhost'
port = 9050

def create_socket(host,port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind((host,port))
    sk.listen(5)
    return sk

def create_data(data):
    data = data +'\0'
    data = data.encode('utf-8')
    return data

def send_data(sk, data):
    data1 = create_data(data)
    sk.sendall(data1)
    
# tra ve data da loai bo '\0'
def recv_data(sk):
    data = bytearray()
    msg = ''
    while not msg:
        data1 = sk.recv(1024)
        if not data1:
            raise ConnectionAbortedError()
        data = data + data1
        if b'\0' in data1:
            msg = data.rstrip(b'\0')
    
    msg = msg.decode('utf-8')
    return msg

def process_client(sk, addr):
    try:
        msg = recv_data(sk)
        split_msg = msg.split()
        loto = []
        if split_msg[0] == 'loto':            
            for i in range(int(split_msg[1])):
                loto.append(random.randint(0, 99))
            print('{}:{}'.format(addr, loto))
            my_string = '-'.join(str(i) for i in loto)
        else:
            my_string = msg
        send_data(sk, my_string)
    except ConnectionError():
        print('error')
    finally:
        sk.close()
            
if __name__=='__main__':
    sk1 = create_socket(host, port)
    local_addr = sk1.getsockname()
    print('local address: {}'.format(local_addr))
    while True:
        client_sk, client_addr = sk1.accept()
        print('client address: {}'.format(client_addr))
        thread = threading.Thread(target=process_client,args=(client_sk, client_addr))
        thread.daemon = True
        thread.start()
