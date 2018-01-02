# Author guomin
#**kewgs把N个关键字参数，转换成字典的方式
def test(**kwargs):
    print(kwargs)
test(name="Lee",age=8,sex="F")
test(**{'name':'Lee','age':8,'sex':'F'})