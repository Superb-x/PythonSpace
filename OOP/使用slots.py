class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'LXL'
s.age = 21
#s.score = 98   #这个时候我们可以发现   score这个属性是不能被添加到实例当中去的,注意slots只对当前的实例生效

class GraduatedStudent(object):
    pass

g = GraduatedStudent()
g.score = 99
print(g.score)

