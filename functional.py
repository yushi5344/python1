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