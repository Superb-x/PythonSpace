#Python内建的模块itertools提供了非常有用的用语操作迭代对象的函数
#首先我们看看itertools提供的几个‘无限’迭代器

import itertools
natuals = itertools.count(1)
# for n in natuals:
#     print(n)    #这样会无限迭代下去

cs = itertools.cycle('ABC')
#for x in cs:
#    print(x)   #同样停不下来

#repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
ns = itertools.repeat('ABC', 3)
for x in ns:
    print(x)

#无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。

#无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
natual = itertools.count(1)
n = itertools.takewhile(lambda x: x <= 10, natual)
print(list(n))

#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC', 'XYZ'):
    print(c)

#groupby()把相邻的重复元素挑出来放在一起:
for key, group in itertools.groupby('AAABBBCCCDDDEEE'):
    print(key + ':  ', list(group))