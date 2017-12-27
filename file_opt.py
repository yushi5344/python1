# Author guomin
# f=open('test',encoding="utf-8")
# data=f.read()
# print(data)
# b=open('test2','w',encoding='utf-8')
# b.write("我爱北京天安门\n")
# b.write("天安门上太阳升")
# c=open("test",'a',encoding="utf-8")
# c.write("when i was young ")
f=open('test','r',encoding="utf-8")
# for index,line in enumerate(f.readlines()):
#     print(line.strip())
#     if index>9:
#         break;
for line in f:
    print(line)