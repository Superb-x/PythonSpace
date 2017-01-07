# -*- coding:utf-8 -*-
from multiprocessing import Process
import os

#子进程要执行的代码
def run_pro(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    p = Process(target=run_pro, args=('test',))   #要注意元组单个参数的写法 ，在封闭的右括号左边加一个,才是元组，才会将'test'作为一个参数传递
    print('Child process will start')
    p.start()
    p.join()
    print('Chilc process End...')