# Author guomin
def add(a,b,f):
    return f(a)+f(b)
s=add(1,-1,abs)
print(s)