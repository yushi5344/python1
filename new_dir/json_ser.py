# Author guomin
import json
info={
    'name':'lee',
    'age':22
}
f=open('json.txt','w+')
f.write(json.dumps(info))
f.close()
print(1)