# Author guomin
x=1
y=2
z=3
def cal(x,y=3,z=2):
    print(x,y,z)
cal(1,z=4,y=6)
#参数不确定的
#变为元组
def test(*args):
    print(args)
test(1,2,4,56)
test([1,2,4,5,6])
#带*传入list,输出还是元组
test(*[1,2,4,5,6])