# -*- coding:utf-8 -*-
#如果要启动大量的子进程，可以用进程池的方式批量创建子进程
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s run %0.2f seconds' % (name, (end - start)))

if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    p = Pool(4) #Pool的默认大小就是CPU的核心数
    for i in range(8):
        p.apply_async(long_time_task, args=(i,))
    print('Wating for all subprocess done...')
    p.close()
    p.join() #join()方法可以等待子进程结束之后再继续往下运行，通常用于进程间的同步
    print('All process has done')

#从结果可以看出   task0,1,2,3是同时执行的，而task 4要等待前面某个task完成之后才能执行，因为我现在的电脑只有四个核心....