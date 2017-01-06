import os
print(os.name)
#获取系统的详细信息可以调用uname()方法
#print(os.uname())  #注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。

print(os.environ)
print(os.environ.get('path'))