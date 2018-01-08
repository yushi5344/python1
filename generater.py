# Author guomin
#列表生成器
#生成器只有在调用时才会生成相应的数据
#只记录当前位置
#只有一个next方法
b=(i*2 for i in range(100000))
for i in b:
    print(i)
print(b.__next__)