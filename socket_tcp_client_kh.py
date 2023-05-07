import sys
import socket

if __name__=='__main__':
	try:
		sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
		sk.connect(('localhost', 5858))
		sk.send('hello server'.encode('utf-8'))
		data = sk.recv(1024).decode('utf-8')
		print(data)
		while True:
			data = input('Enter message to server: ')
			sk.send(data.encode('utf-8'))
			data_recv = sk.recv(1024).decode('utf-8')
			print(data_recv)
			if not data_recv or data_recv == 'bye':
				sk.close()
				sys.exit()
	except socket.error as e:
		print(e)