import socket

if __name__=='__main__':
    hostname= socket.gethostname()
    print(hostname)
    ip = socket.gethostbyname(hostname)
    print(ip)
    print(socket.gethostbyname_ex('www.google.com'))
    print(socket.gethostbyaddr('8.8.8.8'))
    print(socket.getfqdn('www.google.com'))
    print(socket.getaddrinfo('www.google.com', None, 0, socket.SOCK_STREAM))