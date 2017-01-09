#多任务可以由多个进程完成，也可以由一个进程内的多个线程完成
#我们前面提到了进程是由若干线程组成的，一个进程至少有一个线程。
#由于线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，Python也不例外，并且，Python的线程是真正的Posix Thread，而不是模拟出来的线程
#Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。

#启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
import time, threading

#新线程执行的代码
def loop():
    print('thread %s is running' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended' % threading.current_thread().name)

# 多线程和多进程最大的不同在于，多进程中，同一个变量，同一个变量各自有一份拷贝存在每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，所以任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改变一个变量，把内容给改乱了
#来看看多个线程同时操作一个变量怎么把内容给改乱了：

#假设这是你的银行存款
balance = 0
lock = threading.Lock()

def change_it(n):
    #先存后取，结果应该为0
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        #首先要获取金额
        lock.acquire()
        try:
            #放心的改吧
            change_it(n)
        finally:
            #改完一定要释放出去
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

# 执行结果是预想中的0，但是当线程交替执行的时候就会出乱子了。所以要使用lock()方法

