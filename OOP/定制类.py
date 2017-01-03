class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
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


#如果想实现切片的功能,那么需要定义__getitem__方法
class Fib2(object):
    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
        return a

#处理之后就能按下标访问任意一项了、
f = Fib2()
for x in range(21):
    print(f[x])