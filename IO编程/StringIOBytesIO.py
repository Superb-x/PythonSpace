#很多时候数据不一定是文件，也可以在内存中读写 StringIO

from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())
#getvalue 方法用来获得写入后的str
#要读取StringIO，可以用一个str初始化StringIO，然后像文件一样读取

f2 = StringIO('Hello\nHi\nGoodbye!')
while True:
    s = f2.readline()
    if s == '':
        break
    print(s.strip())

#StringIO只能操作str，要操作二进制数就只能靠BytesIO了
from io import BytesIO
f3 = BytesIO()
f3.write('中文'.encode('utf-8'))
print(f3.getvalue())

f4 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f4.read()
print(f4.read())

