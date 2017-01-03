class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
<<<<<<< HEAD
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
=======
        return 'Student Obkect (name: %s)' % self.name
    __repr__ = __str__
print(Student('LXL'))
s = Student('LXL')
s

#如果想让一个类能够被for...in循环遍历，就必须实现一个__iter__方法,使用该方法会返回一个可迭代的对象，然后Python的for循环就会不断的调用该迭代对象的__next__()方法拿到循环的下一个值,直到遇到了stopIteration后退出

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

for x in Fib():
    print(x)


#如果想实现像list、tuple那样的功能,那么需要定义__getitem__方法
class Fib2(object):
    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
        return a

#处理之后就能按下标访问任意一项了、
f2 = Fib2()
for x in range(21):
    print(f2[x])

#如果想实现切片的功能
class Fib3(object):
    def __getitem__(self, item):
        if isinstance(item, int): #判断如果是一个整数类型
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice): #如果是一个切片类型
            start = item.start
            stop = item.stop
>>>>>>> 4701e7805bb9517bc21998c9fc81185a9771c3ed
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
<<<<<<< HEAD
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
=======
                L.append(a)
                a, b = b, a + b
            return L

#照这样处理之后就可以对class进行切片操作了
f3 = Fib3()
print(f3[0:5])

#正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错，比如定义Studdent类
class Student2(object):
    def __init__(self):
        self.name = 'LXL'

#当类有当前的属性或方法时，没问题，如果没有的话就会报错了
s2 = Student2()
print(s2.name)
#print(s2.score) #因为class没有这个属性或方法  所以程序运行的时候回报错
#要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态的返回一个属性，修改之后如下
class Student3(object):
    def __init__(self):
        self.name = 'LXL'
    def __getattr__(self, attr):
        if attr == 'score':
            return 'you have got a 0'

s3 = Student3()
print(s3.score)

#当然也可以返回一个函数，只是需要改变一下调用的方式
class Student4(object):
    def __init__(self):
        self.name = 'LXL'
    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 23
        raise AttributeError('\'student\' object has no attribute \'%s\'' % attr)
s4 = Student4()
print(s4.age())

#一个对象实例可以有自己的属性或者方法，当我们调用方法时，我们用instance.method()来调用，能不能直接在实例本身上直接调用呢？在Python中，答案是肯定的
#任何类，只需要定义一个__call__方法，就可以直接对实例进行调用，请看实例
class Student5(object):
    def __init__(self):
        self.name = 'LXL'
    def __call__(self, *args, **kwargs):
        print('My name is %s' % self.name)

s5 = Student5()
s5()  #这样定义的话就可以直接调用实例本身


#如何去判断一个对象是函数还是对象呢，可以通过callable方法来判定，能被调用就是一个callable对象。通过callable对象我们就能判定对象是不是可调用的对象
print(callable([1,2,3,4]))
>>>>>>> 4701e7805bb9517bc21998c9fc81185a9771c3ed
