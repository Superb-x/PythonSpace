#如果你不幸拥有一个多核CPU，你肯定在想，多核应该可以同时执行多个进程
#如果写一个死循环的话，会出现什么情况

#尝试用Python写一个死循环
import threading, multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()