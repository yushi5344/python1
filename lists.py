# Author guomin
name=["张三","李四","王五","马六","小七"]
# print(name)#列表
# print(name[0],name[2])
# print(name[0:3])#切片
# print(name[1:3])#从第二个开始去完第三个
# print(name[::3])
# print(name[-1])#取倒数第一个值
# print(name[-2:])#从倒数第二个开始取到末尾
#追加到列表最后
name.append("大哥")
print(name)
#添加到列表某个位置
name.insert(2,"小迪")#把小迪插到第三个值上
print(name)
#直接更改
name[0]="张三三";
print(name)
#删除某个值
name.remove("李四")
print(name)
del name[2]#删除第三个值
print(name)
name.pop(1)#删除第二个值
print(name)
print(name.index("马六"))#通过值找到位置
name.reverse()#列表反转
print(name)
print(name.count("马六"))#统计某个值出现的次数
names=name.copy()#复制一个列表
print(names)
name2=name[::2]
for i in name2 :
    print(i)