#colletions是Python内建的一个集合模块，提供了许多有用的集合类
#namedtuple
#我们知道tuple可以表示不变的集合，例如，一个二维坐标系
#p = (1, 2)
#但是，看到(1, 2)，很难看出这个tuple是用来表示一个坐标的。定义一个class又小题大做了，这时，namedtuple就派上了用场：
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)
print(isinstance(p, Point))
print(isinstance(p, tuple))

#namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素，这样一来，我们用namedtuple可以很方便的定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用。

#deque
#使用list存数据时，按索引访问元素很快，但是插入和删除就比较慢，因为list是线性存储，数据量大的时候插入和删除效率就比较低，deque是为了高效实现插入和删除操作的双向列表，适用于队列和栈

from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
#deque除了实现了list的append()和pop()之外，还支持appendleft(), popleft()，这样就可以很高效的在头部添加或者删除数据

#defaultdict
#使用dict时，如果引用的key不存在，就会抛出KeyError。如果希望key不存在的时候返回一个默认值，就可以用defaultdict

from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])   #当访问一个不存在的key值时会返回一个默认值

#OrderedDict
#使用dict时，Key是无序的。在对dict做迭代时，我们无法确定key的顺序，要让key保持顺序，可以用OrderedDict
from collections import OrderedDict
ddd = dict([('a', 1), ('b', 2), ('c', 3)])
print(ddd)   #打印出来可以看到是一个无序的
odd = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(odd)
#要注意的一点是，OrderedDict会按照插入的顺序排列，不是key本身排序
od = OrderedDict()
od['x'] = 1
od['z'] = 2
od['y'] = 3
print(list(od))

#Counter
#Counter是一个简单的计数器，比如说统计字符出现字数

from collections import Counter
c = Counter()
for ch in 'lxl want to be full stack engineer':
    if ch != ' ':
        c[ch] = c[ch] + 1

print(dict(c))