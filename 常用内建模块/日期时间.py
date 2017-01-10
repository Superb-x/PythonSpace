#datetime 是Python处理日期和时间的标准库
from datetime import datetime
import time
for i in range(3):
    now = datetime.now()
    print(now)
    time.sleep(1)

#要获取指定时间，我们直接用参数构造一个datetime
dt = datetime(2017, 1, 10 ,12, 21, 58)
print(dt)

#datetime转换成timestamp
#在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。时间戳，转换的方法也很简单timestamp()
print(dt.timestamp())

#timestamp转换成datetime 使用fromtimestamp()方法即可
t = 1484022118.0
print(datetime.fromtimestamp(t))  #格林尼治天文台与北京相差八个小时
#当然也可以被转换成格林尼治时间
print(datetime.utcfromtimestamp(t))

#str转换成datetime
curDay = datetime.strptime('2017-1-10 14:39:45', '%Y-%m-%d %H:%M:%S')
print(curDay)