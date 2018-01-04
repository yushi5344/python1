# Author guomin
import time
def timmer(func):
    def warpper(*args,**kwargs):
        start_time=time.time()
        func()
        stop_time=time.time()
        print('the func run time is %s' %(stop_time-start_time))
    return warpper
@timmer
def test():
    time.sleep(3)
    print('in the test')
test()
#实现装饰器
#1.函数即变量
#2.高阶函数
#3嵌套函数
#高阶函数+嵌套函数===装饰器