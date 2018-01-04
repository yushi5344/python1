# Author guomin
#高阶函数特点：返回值中包含函数名,不修改函数的调用方式
import time
def bar():
    time.sleep(3)
    print('in the bar')
def test(func):
    print(func)
    return func
bars=test(bar)
bars()