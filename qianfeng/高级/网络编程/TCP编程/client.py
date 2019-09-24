
import socket

client  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('192.168.88.244',8081))


while True:

	data = input("please input send to server message:")
	client.send(data.encode('utf-8'))
	
	info = client.recv(1024)
	print("server recv:",info.decode('utf-8'))