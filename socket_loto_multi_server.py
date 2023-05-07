import socket 
import random
import threading

def generate_random_array(n):
    arr = []
    for i in range(n):
        num = random.randint(0, 99)
        if num < 10:
            arr.append("0" + str(num))
        else:
            arr.append(str(num))
    return arr

def handle_client(client_sk, client_addr):
    print('Client connected from: ', client_addr)
    data = "hello client"
    client_sk.send(data.encode('utf-8'))
    data = client_sk.recv(1024)
    print(data.decode('utf-8'))
    while True:
        data = client_sk.recv(1024)
        temp = data.decode('utf-8')
        print(temp)
        if ("loto" in temp):
            num = int(temp.split()[1])
            separator = ', '
            arr = generate_random_array(num)
            string = separator.join(str(num) for num in arr)
            client_sk.send(string.encode('utf-8'))
        else:
            client_sk.send(data)
        if not data or temp == 'bye':
            break
    client_sk.close()
    print('Client disconnected from: ', client_addr)

if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind(('127.0.0.1', 9050))
    sk.listen(5)
    while True:
        client_sk, client_addr = sk.accept()
        t = threading.Thread(target=handle_client, args=(client_sk, client_addr))
        t.start()
