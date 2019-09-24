import socket

# 建立socket连接
udpServer = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 绑定IP，监听端口
udpServer.bind(('192.168.88.244',8080))

while True:
	data,addr = udpServer.recvfrom(1024)
	
	print('客户端说：',data.decode('utf-8'))
	data = input("输入数据")
	
	udpServer.sendto(data.encode("utf-8"),addr)

