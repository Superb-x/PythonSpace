# -*- coding:utf-8 -*-
#很多时候子进程并不是自身，而是一个外部进程。我们创建一个子进程后，还需要控制子进程的输入和输出
import subprocess

print('# nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit Code:', r)

#如果子进程还需要输入
print('# nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
