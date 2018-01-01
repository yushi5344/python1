# Author guomin
import sys
#打印系统默认编码
print(sys.getdefaultencoding())
s="你好"
print(s.encode('GBK'))
print(s.encode())