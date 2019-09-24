import socket

# 创建socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 绑定IP和端口
server.bind(('192.168.88.244',8081))

# 监听
server.listen(5)

print("服务器启动成功")

# 等待连接
clientSocket,clientAddress = server.accept()

while True:
	# 接收数据
	data = clientSocket.recv(1024)
	print("收到"+ str(clientSocket) + "的数据" + data.decode('utf-8'))
	
	# 返回数据
	clientSocket.send('hello'.encode('utf-8'))
