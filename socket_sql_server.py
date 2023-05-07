import pyodbc
import socket
import threading

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DUNNO\SQLEXPRESS;'
                      'Database=DuLieu;'
                      'Trusted_Connection=yes;')

def func1(client_sk, client_addr):
        print('client address: {}'.format(client_addr))
        try:
            data = recv_data(client_sk)
            print('{}:{}'.format(client_sk, data))
            
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Khach')
            result = cursor.fetchall()
            x = ""
            for r in result:
                x = x + str(r)
            x = x + '\0'
            cursor.close()
            conn.close()
            send_data(client_sk, x)
            client_sk.close()
        except ConnectionError:
            print("Error")
        finally:
            client_sk.close()
        

def create_socket(host, port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind((host, port))
    sk.listen(5)
    return sk

def create_data(data):
    return data.encode('utf-8')

def send_data(sk, data):
    data1 = create_data(data)
    sk.sendall(data1)
    
def recv_data(sk):
    data = bytearray()
    msg = ''
    while not msg:
        data1 = sk.recv(1024)
        if not data1:
            raise ConnectionError()
        data = data + data1
        if b'\0' in data1:
            msg = data.rstrip(b'\0')
    msg = msg.decode('utf-8')
    return msg

if __name__ == '__main__':
    sk1 = create_socket('localhost', 9050)
    local_addr = sk1.getsockname()
    print('local_addr: {}'.format(local_addr))
    
    while True:
        client_sk, client_addr = sk1.accept()
        t1 = threading.Thread(target=func1, args = (client_sk, client_addr))
        t1.start()
       
    
            
            
            
            
            
            
            
            
            
            
            
            