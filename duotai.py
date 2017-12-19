class Person(object):
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    def whoAmI(self):
        return 'I am a Person,my name is %s' % self.name
class Studends(Person):
    def __init__(self,name,gender,score):
        super(Studends,self).__init__(name,gender)
        self.score=score
    def WhoImI(self):
        return 'I am a Student,my name is %s' %self.name
class Teachers(Person):
    def __init__(self,name,gender,age):
        super(Teachers,self).__init__(name,gender)
        self.age=age
    def whoAmI(self):
        return 'I am a Teacher,my name is %s' % self.name
def who_am_i(x):
    print(x.whoAmI())
p=Person('Tim','Male')
s=Studends('Boc','Male',99)
t=Teachers('Lily','Female',44)
who_am_i(p)
who_am_i(s)
who_am_i(t)

