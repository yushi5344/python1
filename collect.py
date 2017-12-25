# Author guomin
list_1=[1,2,3,4,5,6,7,8]
list2=set(list_1)#集合也是无序的
#print(list2,type(list_1))
list3=set([1,34,23,4,22,18,6])
print(list2,list3)
print(list2.intersection(list3))#交集
print(list2.union(list3))#并集
#差积
print(list3.difference(list2))
#子集
list4=set([1,4,6])
print(list3.issubset(list4))
print(list4.issubset(list3))
print(list3.issuperset(list4))
#对称差积,去掉两个集合中相同的
print(list2.symmetric_difference(list3))
#符号
print(list2 & list3)#交集
print(list2 | list3) #并集
print(list2-list3)#在集合2但不在集合3中
print(list2^list3)#对称差积
list3.add(8)
print(list3)
list3.remove(22)
print(list3)
print(len(list3))
print(8 in list3)
list3.pop()
print(list3)#删除
list3.discard(18)#删除指定值
print(list3)