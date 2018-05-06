# Author guomin
def bulk(self):
    print('%s is yelling'%self.name)

class Dog(object):
    def __init__(self,name):
        self.name=name

    def eat(self,food):
        print('%s is eating'%self.name,food)

d=Dog('Jack')
choice=input(">>:").strip()

if hasattr(d,choice):
    func=getattr(d,choice)
    func('rice')
else:
    setattr(d,choice,bulk)
    d.talk(d)