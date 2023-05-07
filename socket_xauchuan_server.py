import socket

if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind(('127.0.0.1', 9050))
    sk.listen(10)
    print("waiting...")
    client_sk, aclient_addr = sk.accept()
    s = 'hello client'
    client_sk.send(s.encode('utf-8'))
    data = client_sk.recv(1024)
    print(data.decode('utf-8'))

    while True:
        dl = client_sk.recv(1024)
        if not dl or dl.decode('utf-8') == 'bye':
            break
        else:
            arr = dl.decode('utf-8')
            index = 0
            for i in range(0, len(arr)):
                if arr[i] != '.' and arr[i] != ',' and arr[i] != ' ':
                    index = i
                    break
            str = arr[index].upper()
            for i in range(index + 1, len(arr)):
                if arr[i] == '.':
                    if str[len(str) - 1] != '.':
                        str = str + arr[i] + " "
                elif arr[i] == ',':
                    if str[len(str) - 1] != ',':
                        str = str + arr[i] + " "
                elif arr[i] == ' ':
                    if str[len(str) - 1] != ' ':
                        if arr[i + 1] != ' ' and arr[i + 1] != ',' and arr[i + 1] != '.':
                            str = str + arr[i]
                else:
                    if str[len(str)-2]=='.':
                        str = str + arr[i].upper()
                    else:
                        str = str + arr[i].lower()
            print(str)
            client_sk.send(str.encode('utf-8'))
        client_sk.close()
        sk.close()
