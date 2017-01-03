class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student Object (name: %s)' % self.name
    __repr__ = __str__


s = Student('LYL')
s
print(Student('LXL'))

#如果一个class想被用于for...in循环，类似list或tuple那样，那必须实现一个__iter__()方法，该方法返回一个迭代对象，然后Python的for循环就会不断的调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到stopIteration错误时退出循环
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self #实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:  #这是退出循环的条件
            raise StopIteration()
        return self.a

for n in Fib():
    print(n)

#让class表现的像list那样照下标取出元素，需要实现__getitem__()方法

class Fib2(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


#这样的话就可以按下标访问任何一项了
f = Fib2()
print(f[0:5])

#改造之后Fib2也能切片了


#__getattr__方法  正常情况下如果我们调用类的方法或属性时，如果不存在，就会报错，比如定义一个car类
class Car(object):
    def __init__(self):
        self.name = 'BMW'
    def __getattr__(self, item):
        if item == 'price':
            return 'I dont konw'
c = Car()
print(c.name)
#当调用有的属性时是没问题的
print(c.price) #调用不存在的属性时就会报错了