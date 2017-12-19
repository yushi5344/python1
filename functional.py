# def add(x,y,f):
#     return f(x)+f(y)
# s=add(-4,5,abs)
# print(s)
import math
from functools import reduce
# def add(x,y,f):
#     return f(x)+f(y)
# s=add(4,9,math.sqrt)
# print(s)
# def fu(x):
#     return x*x
# print(map(fu,[1,2,3,4,5,6,7,8,9]))
# def toFisrtUpper(x):
#     return x[0].upper()+x[1:].lower()
# s=list(map(toFisrtUpper,['adam','LISA','barT']))
# print(s)
# def d(x,y):
#     return x*y
# s=reduce(d,[2,4,5,7,12])
# print(s)
# def is_odd(x):
#     return x%2==1
# s=list(filter(is_odd,[1,2,3,4,5,6,7,8,9]))
# print(s)
# def squares(x):
#     r=int(math.sqrt(x))
#     return r*r==x
# s=list(filter(squares,range(1,101)))
# print(s)
# print(sorted([35,6,12,9,21]))
def reversed_cmp(x,y):
    if x>y:
        return -1
    elif x<y:
        return 1
    else:
        return 0
L=[('b',2),('a',1),('c',3),('d',4)]
students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
# print(sorted(L,cmp=lambda x,y:cmp(x[1],y[1])))
# print(sorted(students, key=lambda s: s[2], reverse=True))
# def tolower(x):
#     return x.lower()
# s=sorted()
# def cmp_ignore_case(s1, s2):
#     u1 = s1.upper()
#     u2 = s2.upper()
#     if u1 < u2:
#         return -1
#     if u1 > u2:
#         return 1
#     return 0
# print( sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case))
# def calc_prod(lst):
#     def alls():
#         s=1
#         for i in lst:
#             s=s*i
#         return s
#     return alls
# alls=calc_prod([1,2,3])
# print(alls())
# def count():
#     fs=[]
#     for i in range(1,4):
#         def f(j):
#             def g():
#                 return j*j
#             return g
#         r=f(i)
#         fs.append(r)
#     return fs
# f1,f2,f3=count()
# print(f1())
# s=map(lambda x:x*x,[1,3,4,5,6,7,8])
# print(list(s))
# s=sorted([1,23,5,6,14,90,2],lambda x,y:-cmp(x,y))
# print(s)
# def is_not_empty(s):
#     return s and len(s.strip())>0
# s=filter(is_not_empty,['test','None','','str','   ','END'])
# print(list(s))
# h=filter(lambda s:s and len(s.strip())>0,['test','None','','str','   ','END'])
# print(list(h))
# print(math.pow(2,0.5))
# import logging
# print(math.log(10))
# print(logging.log(10,'something'))
# try:
#     import simplejson as json
# except ImportError:
#     import json
# print(json.dumps({'python':3.6}))
# class Person(object):
#     pass
# xiaoming=Person()
# xiaoming.name='Xiao Ming'
# xiaoming.gender='Male'
# xiaoming.birth='22-11'
# xiaohong=Person()
# xiaohong.name='Xiao Hong'
# xiaohong.grade=4
# xiaoming.grade=xiaohong.grade+1
# print(xiaohong)
# print(xiaoming)
# print(xiaoming==xiaohong)
import types
class Person(object):
    __address='china'
    def __init__(self,name,score,**kwargs):
        self.name=name
        # self.gender=gender
        # self.__birth=birth
        self.score=score
        for k,v in kwargs.items():
            setattr(self,k,v)
    # def get_grade(self):
    #     if self.__score>90:
    #         x='优秀'
    #     elif self.__score>70 and self.__score<=90:
    #         x='及格'
    #     else:
    #         x='不及格'
    #     return x
# xiaoming=Person('Xiao Ming','Male','1991-1-1')
# xiaohong=Person('Xiao Hong','FeMale','1994-2-2',job='student')
# print(xiaohong.name)
# print(xiaohong.job)
# print(xiaohong.birth)
# print(xiaohong.address)
p1=Person('xiao li',99)
p2=Person('xiao wang',78)
# print(p1.get_grade())
# print(p2.get_grade())
# print(p1.get_grade)
def get_grade(self):
    if self.score > 90:
        x = '优秀'
    elif self.score > 70 and self.score <= 90:
        x = '及格'
    else:
        x = '不及格'
    return x
p1.get_grade=types.MethodType(get_grade,p1)
print(p1.get_grade())