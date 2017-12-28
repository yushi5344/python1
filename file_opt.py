# Author guomin
# f=open('test',encoding="utf-8")
# data=f.read()
# print(data)
# b=open('test2','w',encoding='utf-8')
# b.write("我爱北京天安门\n")
# b.write("天安门上太阳升")
# c=open("test",'a',encoding="utf-8")
# c.write("when i was young ")
#f=open('test','r+',encoding="utf-8")
# for index,line in enumerate(f.readlines()):
#     print(line.strip())
#     if index>9:
#         break;
# for line in f:
#     print(line)
#ileno())#文件在内存中的编号
import sys,time
# for i in range(20):
#     sys.stdout.write('#')
#     sys.stdout.flush()#内存中刷新输出
#     time.sleep(0.5)
#f.truncate(20)
#f=open('test','W+',encoding='utf-8')#写读  先写后读
f=open('test3','wb')
f.write('Hello world'.encode())
f.close()