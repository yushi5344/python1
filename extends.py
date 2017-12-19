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
