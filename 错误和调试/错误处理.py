def foo():
    r = some_function()
    if r == (-1):
        return (-1)
    #dosomething
    return r

def bar():
    r = foo()
    if r == (-1):
        print('Error')
    else:
        pass

#程序运行的过程中如果发生了错误，就可以事先约定返回一个错误代码，这样，就可以知道是否有错，以及出错的原因
#1、try机制
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:  #ZeroDivisionError 意思是浮点溢出   除数为 0 的时候会报的一个错误
    print('except:', e)
finally:
    print('finally...')
print('END')

#上述代码在运行时会产生一个除法错误,如果将除数改成2就不会有问题
try:
    print('try...')
    r = 10 / 2
    print('result:', '%.5f' % r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('End')

#当然可以有多个except来捕获不同类型的错误
try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:  #如果没有错误的话就会执行这一个语句块
    print('No Error!')
finally:
    print('finally...')
print('End')

#Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。比如：
try:
    foo()
except ValueError as e:
    print('ValueError')
except UnicodeError as e: #UnicodeError 是ValueError的子类,所以第一个被捕获之后，这一块就捕获不到了  相关文档https://docs.python.org/3/library/exceptions.html#exception-hierarchy
    print('UnicodeError:', e)

#try...except捕获还有一个巨大的好处就是可以跨越多层调用
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

#这样的话就只需要在可能出现错误的地方去捕获而不用去整个的捕获，主要也是为了节省内存


