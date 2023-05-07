import socket

if __name__=='__main__':
	try:
		sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
		sk.bind(('localhost', 5858))
		sk.listen(5)
		client_sk, client_addr = sk.accept()
		data = client_sk.recv(1024).decode('utf-8')
		print(data)
		client_sk.send('hello client'.encode('utf-8'))
		while True:
			data = client_sk.recv(1024).decode('utf-8')
			print(data)
			if not data or data == 'bye':
				client_sk.close()
				break
			data_send = input('Enter message to client: ')
			client_sk.send(data_send.encode('utf-8'))
		sk.close()
	except socket.error as e:
		print(e)