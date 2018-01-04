# Author guomin
#高阶函数
#① 把一个函数名当做参数传递给另一个函数
import time
def bar():
    time.sleep(3)
    print('in the bar')

def test(func):
    start_time=time.time()
    func()
    stop_time=time.time()
    print('函数运行时间 %s' %(stop_time-start_time))

test(bar)