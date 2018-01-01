# Author guomin
with open('test','r',encoding="utf-8") as f,\
    open('test2','r',encoding="utf-8") as f2:
    for line in f:
        print(line)
    for h in f2:
        print(h)