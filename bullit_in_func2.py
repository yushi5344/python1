# Author guomin
print(hex(10))
print(oct(8))
print(pow(2,8))#2的8次方
print(round(1.44442,2))
print(slice(2,5,None))
a={6:2,8:0,1:4,-5:6,99:11,4:22}
print(sorted(a.items()))#按key
print(sorted(a.items(),key=lambda x:x[1])) #按value排序
a=[1,2,3,4]
b=['a','b','c','d','e']
z=zip(a,b)#两个list合并
for i in z:
    print(i)