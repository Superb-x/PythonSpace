#如果要抛出错误，首先需要根据需要定义一个错误class,选择好继承关系，然后，用raise语句抛出一个错误的实例
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')

#再看另一种错误处理方式

def foo2(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar2():
    try:
        foo2('0')
    except ValueError as e:
        print('ValueError')
    raise

bar2()
#其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理。
#raise 语句如果不带参数，就会把错误原样抛出，此外，在except中raise一个Error，还可以把这一种类型的错误转化成另一种类型
try:
    10 / 0
except ZeroDivisionError as e:
    raise ValueError('input Error')

#只要是合理的转换逻辑就可以，绝对不能把一个IOError转换成一个毫不相干的ValueError