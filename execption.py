# Author guomin

data={}
names=['Jack','Bob']
try:
    names[3]
    data['name']

except (KeyError,IndexError) as e:
    print('没有这个key',e)
except Exception as e:
    print('未知错误',e)


else:
    print('一切正常')

finally:
    print('不管有没有错，都执行这句')

#捕获索引错误
#except Exception as e

