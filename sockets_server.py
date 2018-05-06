# Author guomin
import socket
server=socket.socket()
server.bind(('localhost',6969))
server.listen()
print('我要开始等电话了')
conn,addr=server.accept() #等待
# conn就是客户端连过来而在服务器端生成的一个连接实例
print('等到了')
while True:
    data=conn.recv(1024)
    print('rece_server',data)
    conn.send(data.upper())

server.close()