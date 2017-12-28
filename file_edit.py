# Author guomin
f=open('test','r',encoding="utf-8")
f_ew=open('test_new','w',encoding="utf-8")
for line in f:
    if "Was blind but now i see" in line:
        line=line.replace("Was blind but now i see","hhhhhhhhWas blind but now i see")
    f_ew.write(line)
f.close()
f_ew.close()