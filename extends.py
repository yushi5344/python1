class Person(object):
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
class Students(Person):
    def __init__(self,name,gender,score):
        super(Students,self).__init__(name,gender)
        self.score=score
class Teachers(Person):
    def __init__(self,name,gender,age):
        super(Teachers,self).__init__(name,gender)
        self.age=age
p=Person('Tim','Male')
s=Students('Bob','Male',55)
t=Teachers('Alice','Female',22)
print(isinstance(p,Person))
print(isinstance(p,Students))
print(isinstance(t,object))
print(isinstance(t,Person))
print(isinstance(t,Students))
print(isinstance(t,Teachers))
