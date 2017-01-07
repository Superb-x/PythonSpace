# -*- coding:utf-8 -*-
#在程序的运行过程中，所有变量都是在内存中，比如，定义一个dict
d = dict(name='Bob', age=22, score=88)
d['name'] = 'LXL'
print(d['name'])
#首先需要搞清楚序列化是一个什么概念  我们把变量从内存中编程可以存储或者传输的过程称之为序列化，在Python中叫做picking，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。序列化之后，就可以把序列化之后的内容写入磁盘，或者通过网络传输到别的机器上，反过来，把变量内容从序列化的对象重新读到内存里叫做反序列化，即unpicking,Python中提供了pickle模块来实现序列化
import pickle

f = dict(name = 'LYL', age = 21, score = 99)
pickle.dumps(f)
w = open('picking.txt', 'wb')
pickle.dump(f, w)
w.close()
f = open('picking.txt', 'rb')
d = pickle.load(f)  #看似是回来了   其实这两个变量是一个毫不相关的变量只是内容相同而已
f.close()
print(d)