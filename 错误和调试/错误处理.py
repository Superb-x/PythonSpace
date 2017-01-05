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
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')