# Author guomin
#局部作用域和全局作用域的访问顺序
x=0
def grandpa():
    def dad():
        x=2
        def son():
            x=3
            print(x)
        son()
    dad()
grandpa()