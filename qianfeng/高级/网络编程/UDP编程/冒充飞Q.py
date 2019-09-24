
'''
TCP是建立可靠地连接，并且通信双方都可以用流的形式发送数据
相对TCP，udp则是面向无连接的协议

使用udp协议时，不需要建立连接，只需要知道对方的ip地址和端口号，
就可以直接发送数据包，但是能不能到达就不知道了

虽然udp传输数据不可靠，但是他的优点和TCP相比，数据传输速度快
'''

import socket

# a是账号 288后面是发送内容
str = "1_1bt4_10#32499#002481627512#0#0#0:1289671407:a:b:288:hjll is a good man"

udp = socket.socket(socket.AG_INET,socket.SOCK_DGRAM)
udp.connect(("192.168.88.244",2425))
udp.send(str.encode('utf-8'))