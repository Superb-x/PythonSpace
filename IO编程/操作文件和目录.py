import os
print(os.name)
#获取系统的详细信息可以调用uname()方法
#print(os.uname())  #注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。

print(os.environ)
print(os.environ.get('path'))
#查看当前目录的绝对路径
print(os.path.abspath('.'))
#在某个目录下创建新目录，首先需要把目录的完整路径先表示出来
n = os.path.join('D:\PythonWorkspace\IO编程', 'testDir')
#之后创建一个新目录  注意：把两个路径合成一块时要注意不能直接拼接字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符同样的道理，要拆分的时候也不要去直接拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
#>>>os.path.split('D:\PythonWorkspace\IO编程\testDir')
#('D:\PythonWorkspace\IO编程','testDir')
#当然也有更简便的方法
#>>>os.path.splitext()可以直接得到文件扩展名  注意是文件扩展名  也就是文件后缀
#>>>os.path.splitext('\path\to\file.txt')
#('path\to\file', '.txt')
#
#os.mkdir(n)
#之后删掉一个目录
#os.rmdir(n)
#对文件重命名
#os.rename('test.txt', 'test.py')
#删除文件
#os.remove('test.py')
print(list(x for x in os.listdir('.') if os.path.isdir(x)))
print(list(x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)))
