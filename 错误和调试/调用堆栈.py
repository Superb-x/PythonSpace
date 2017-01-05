#调用堆栈  如果错误没有被捕获，错误就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后退出程序
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     bar('0')
#
# main()

#Python内置的logging模块可以非常容易的记录错误信息:
import logging

def foo2(s):
    return 10 / int(s)

def bar2(s):
    return foo2(s) * 2

def main2():
    try:
        bar2('0')
    except Exception as e:
        logging.exception(e)

main2()
print('End')
