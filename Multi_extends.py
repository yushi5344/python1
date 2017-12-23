class A(object):
    def __init__(self,a):
       print('init A')
       self.a=a
class B(A):
    def __init__(self,a):
        super(B,self).__init__(a)
        print('init B')
class C(A):
    def __init__(self,a):
        super(C,self).__init__(a)
        print('init C')
class D(B,C):
    def __init__(self,a):
        super(D,self).__init__(a)
        print('init D')
# d=D('aaa');
# print(d.a)
class Person(object):
    def __init__(self,name):
        self.name=name
class Student(Person):
    def __init__(self,name):
        super(Student,self).__init__(name)
        self.name=name
class Teacher(Person):
    def __init__(self,name):
        super(Teacher,self).__init__(name)
        self.name=name
class SkillMixin(object):
    def __init__(self,name):
        self.name=name
姓名='maguomin'
print(姓名)
