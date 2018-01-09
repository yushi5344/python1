# Author guomin
print(all([1,-5,3,0]))
print(any([1,-5,3,0]))
print(chr(87))
print(chr(65))
print(chr(98))
print(ord('W'))
print(ord('C'))
code="for i in range(10):print (i)"
compile(code,'','exec')
calc=lambda n:3 if n<4 else n
print(calc(2))
res=filter(lambda n:n>5,range(10))
for i in res:
    print(i)
res=map(lambda n:n*2,range(10))
for i in res :
    print(i)
import functools
res=functools.reduce(lambda x,y:x+y,range(10))
print(res)
a=frozenset([1,2,4,555,212,33,33,12,4])
print(a)
print(globals())