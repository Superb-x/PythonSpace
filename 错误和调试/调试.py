# def foo(s):
#     n = int(s)
#     print('>>>n = %d' % n)
#     return 10 / n
#
# def main():
#     foo('0')
#
# main()

#第二中方式 断言
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero'
    return 10 / n

def main():
    foo('0')

#第三种方式 logging
import logging

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

