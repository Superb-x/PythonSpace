f = open('test.txt', 'r')
print(f.read())
#一定注意在使用完文件之后就关闭掉，不然这样会占用系统的资源，
f.close()

#当然，为了保证无论是否出错都能正确的关闭文件
try:
    f = open('test.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

#Python中有with语句来自动帮我们调用close()
with open('test.txt', 'r') as f:
    print(f.read())

f2 = open('test.txt', 'r')
for line in f2.readlines():
    print(line.strip())
f2.close()

f3 = open('../dingdang.jpg', 'rb')
print(f3.read())
f3.close()

f4 = open('Chinese.txt', 'r', encoding='gbk', errors='ignore')
print(f4.read())

#文件写入
w = open('test.txt', 'w')
w.write('hello,Python')
w.close()

with open('test.txt', 'w') as w2:
    w2.write('hello,Python\nyou are the most beautiful language\n测试中文编码')