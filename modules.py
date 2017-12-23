# Author guomin
# import sys
# print(sys.path)
# print(sys._git)
# print(sys._current_frames())
# print(sys.argv)
import os
#print(os.path)
#os.system("dir")#执行命令，不保存结果
cmd_res=os.popen("dir").read()
print(cmd_res)
#os.mkdir("new_dir")