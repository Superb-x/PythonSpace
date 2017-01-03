class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student Obkect (name: %s)' % self.name
print(Student('LXL'))