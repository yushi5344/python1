# Author guomin
import socket
#这是客户端
client=socket.socket() #生成socket类型，同时生成socket连接对象
client.connect(('localhost',6969))
client.send(b'Hello World')
data=client.recv(1024)
print("rece",data)
client.close()