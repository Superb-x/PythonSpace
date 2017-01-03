class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('error score')
bart = Student('LXL', 1000)
lyl = Student('LYL', 88)

bart.__name = 'New Name'
print(lyl.get_name())
bart.set_score(100)
print(bart.get_score())