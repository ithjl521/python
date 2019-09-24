import socket

'''
客户端：创建TCP链接时，主动发起连接的叫做客户端
服务的：接收服务端的连接
'''

# 1、创建socket
# 参数1：指定协议AF_INET或AF_INET6
# 参数2：指定使用面向流的TCP协议
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


# 2、建立连接
# 参数是一个元组，第一个元素为要连接的服务器IP地址，第二个元素为端口号
sk.connect(("www.sina.com.cn",80))


sk.send(b'GET / HTTP/1.1\r\nHOST:www.sina.com.cn\r\nConnection:close\r\n\r\n')


# 等待接收数据
data = []
while True:
	# 每次接收1K数据
	tempData = sk.recv(1024)
	if tempData:
		data.append(tempData)
	else:
		break;


dataStr = (b''.join(data)).decode('utf-8')
		
# 断开连接
sk.close()

print(dataStr)