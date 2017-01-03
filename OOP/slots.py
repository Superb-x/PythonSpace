class Student(object):
    pass

s = Student()
s.name = 'LXL'
print(s.name)

def set_age(self, age):
    self.age = age

from types import MethodType

s.set_age = MethodType(set_age, s)
s.set_age(21)
print(s.age)

s2 = Student()


def set_score(self, score):
    self.score = score

Student.set_score = set_score


s.set_score(98)
s2.set_score(88)

print(s.score)
print(s2.score)