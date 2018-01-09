# Author guomin
#可以用于for循环的对象称为可迭代对象
#可以被next()函数调用并不断返回下一个值的对象称为迭代器
from collections import Iterable
print(isinstance([],Iterable))#可迭代对象
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))#不5是可迭代对象
from collections import Iterator
print(isinstance([],Iterator))
#list,dict,str等Iterable都是可迭代对象，但不是迭代器
#将list,dist,str等Iterable变成迭代器
#凡是可作为next（）函数的对象都是Iterator类型
#集合数据类型如list,dict,str等是Iterable但不是Iterator,不过可以通过iter()函数获得一个Iterator对象、
#range()在python3.x中就是一个迭代器
#for i in f 文件读取就是一个迭代器