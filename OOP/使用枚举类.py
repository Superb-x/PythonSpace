#当我们需要定义一个常量的时候，一个办法就是通过用大写变量通过整数来定义，例如月份
# JAN = 1
# FEB = 2
# MAR = 3
# APR = 4
# MAY = 5
# JUN = 6
# JUL = 7
# AUG = 8
# SEP = 9
# OCT = 10
# NOV = 11
# DEC = 12
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

for day in Weekday:
    print(day, '=>',day.value)