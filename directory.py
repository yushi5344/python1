# Author guomin
#字典是无需的
info={
    'stu1101':'张三',
    'stu1102':'李四',
    'stu1103':'王五',
}
print(info)
print(info.values())#获取value
print(info.keys())#获取key
# print(info.get("stu1101"))#获取
# info['stu1104']='aaa'
# print(info)
# info['stu1102']='bbb'
# print(info)
# info.pop('stu1101')#删除
# print(info)
# del info['stu1103']#删除
# print(info)
# info.popitem()#随机删除
# print(info)
b={1:2,3:4,"stu1107":"abc"}
info.update(b)
print(info)
print(info.items())
for key in info:
    print(key,info[key])
for k,v in info.items():
    print(k,v)