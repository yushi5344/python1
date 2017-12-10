age=20
# if age>=18:
#     print('your age is',age)
#     print('adult')
# print('end')
# score=75
# if score>=60:
#     print('passed')
# if age >=18:
#     print('adult')
# else:
#     print('teenger')
#
# score=55
# if score>=60:
#     print('passed')
# else:
#     print('failed')
# if age>=18:
#     print('adult')
# elif age>=6:
#     print('teenger')
# elif age>=3:
#     print('kid')
# else:
#     print('baby')
# if age>=6 and age<18:
#     print('teenger')
# elif age>=18:
#     print('adult')
# else:
#     print('kid')
# score=88
# if score<60:
#     print('failed')
# elif score >=60 and score <80:
#     print('passed')
# elif score >=80 and score<90:
#     print('good')
# elif score>=90:
#     print('excellent')
# L=['adam','lisa','bart']
# for name in L:
#     print(name)
# S=[75,92,59,68]
# sumscore=0
# for score in S:
#     sumscore+=score
# print(sumscore/4)
# N=10
# x=0
# while x<N:
#     print(x)
#     x=x+1
# N=100
# x=1
# sums=0
# while x<N:
#     sums+=x
#     x=x+2
#
# print(sums)
# sum=0
# x=1
# while True:
#     sum=sum+x
#     x=x+1
#     if x>100:
#         break
# print(sum)
# sum=0
# x=1
# n=1
# while True:
#     sum+=x
#     x=x*2
#     n=n+1
#     if n>20:
#         break
# print(sum)
# L=[75,98,59,81,66,43,69,85]
# sum=0
# n=0
# for x in L:
#     if x<60:
#         continue
#     sum=sum+x
#     n=n+1
# print(sum/n)
# sums=0
# x=1
# while True:
#     sums=sums+x
#     x=x+1
#     if not x%2:
#         continue
#     if x>100:
#         break
# print(sums)
# for x in ['a','b','c']:
#     for y in ['1','2','3']:
#         print(x+y)
# M=[1,2,3,4,5,6,7,8,9]
# N=[0,1,2,3,4,5,6,7,8,9]
# for x in M:
#     for y in N:
#         if x<y:
#             print(x,y)
d={
    'adam':95,
    'lisa':85,
    'bart':59
}
# print(len(d))
d.update({'paul':75})
# print(d)
# print(d['adam'])
# print(d.get('bart'))
# print(d.get('aa'))
# print('Adam:',d.get('adam'))
# d['paul']=72
# print(d)
# for key in d:
#     print(key,d[key])
# s=set(['A','B','C','A'])
# print(s)
# h=set(['Adam','Lisa','Bart','Paul'])
# print(h)
# print('bart' in h)
# M=[]
# for x in h:
#     y=x.lower()
#     M.append(y)
# s=set(M)
# print('paul' in s)
months=set(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
# x='Jan'
# y='Fes'
# if x in months:
#     print('x in')
# else:
#     print('x not in')
# if y in months:
#     print('y in')
# else:
#     print('y not in')
# for m in months:
#     print(m)
# s=set([('adam',83),('lisa',88),('bart',99)])
# for h in s:
#     print(h[0],':',h[1])
# s.add('parl')
# print(s)
# s.remove('parl')
# print(s)
# s=abs('a')
# s=int('123')
# s=str(22)
# print(s)
# s=[]
# n=1
# while n<101:
#     s.append(n*n)
#     n=n+1
# print(s)
# print(sum(s))
# print(abs(-100,200))
# def my_abs(x):
#     if x>0:
#         y=x
#     else:
#         y=-x
#     return y
#
# print(my_abs(-10))
# def square_of_sum(L):
#     s=0
#     for i in L:
#         s=s+i*i
#     return s
# s=[1,2,3,4,5]
# print(square_of_sum(s))
import math
# def move(x,y,step,angle):
#     nx=x+step*math.cos(angle)
#     ny=y-step*math.sin(angle)
#     return nx,ny
# x,y=move(100,100,60,math.pi/2)
# r=move(100,100,60,math.pi/2)
# print(x,y)
# print(r)
# print(math.sqrt(4))
#ax*x+bx+c=d
#ax*x+bx+c-d=0
# def quear(a,b,c,d):
#     t=math.sqrt(b*b-4*a*(c-d))
#     y=(-b+t)/(2*a),(-b-t)/(2*a)
#     return y
# y=quear(3,4,5,6)
# print(y)
# def greet(x,y=0):
#     if y:
#         s='Hello',y
#     else:
#         s='Hello,world'
#     return s
# s=greet('a','lisi')
# print(s)
# def greet(name='World'):
#     s='Hello,'+name+'.'
#     return s
# print(greet())
# def average(*n):
#     s=0
#     if len(n)==0:
#         return s
#     for x in n:
#         s=s+x
#     return s/len(n)
# s=average(1,2,3,4,5,6)
# print(s)
# l=['Adam','Lisa','Bart','Paul']
# print(l[0:3])
# print(l[:2])
# print(l[1:2])
# print(l[::2])
# s=range(1,101)
# print(s[:9])
# print(s[2::3])
# print(l[-2:-1])
# print(l[-4:-1:2])
# print(s[-1:-10])
# print(s[-1::])
# h='absdefghijklmn'
# print(h[-7:])
# print(h[-7:-1])
# print(h[-7:-1:2])
# def strUpper(h):
#     s=h[0].upper()+h[1:]
#     return s
# print(strUpper(h))
# l=range(1,100)
# s=0
# h=[]
# for i in l:
#     if s%7==0:
#         h.append(i)
#     s=s+1
# print(h)
# for i in l:
#     h.append(i)
#     s=s+7
# print(h)
# l=['adin','lisa','baft','paul']
# for index,name in enumerate(l):
#     print(index,'--',name)
# s=range(1,5)
# h=zip(l,s)
# print(h)
# for index,name in zip(range(1,len(l)+1),l):
#     print(index,'--',name)
d={'adam':95,'lida':87,'bart':59,'paul':74}
# print(d.values())
# for v in d.values():
#     print(v)
# s=0
# for v in d.values():
#     s=s+v
# h=s/len(d.values())
# print(h)
# print(d.items())
# for key,value in d.items():
#     print(key,':',value)
# s=[x*x for x in range(1,11)]
# print(s)
# s=[str(x)+'x'+str(x+1) for x in range(1,100,2)]
# print(s)
# h=[y for y in range(2,100,2)]
# print(h)
# s=[x*x for x in range(1,11) if x%2==0]
# print(s)
# def toUpper(L):
#     return [x.upper() for x in L if isinstance(x,str)]
# print(toUpper(['Hello','World',101]))
# s=[m+n for m in 'ABC' for n in '123']
# print(s)
h='1234567890'
d='123456789'
s=[x+y+z for x in d for y in h for z in d if x==z ]
print(s)
print(len(s))