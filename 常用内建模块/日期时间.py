#datetime 是Python处理日期和时间的标准库
from datetime import datetime, timedelta
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

#datetime转换成str
cur = datetime.now()
print(cur.strftime('%a, %b %d %H:%M'))

#datetime加减 引入datetime里面的timedelta模块
curr = datetime.now()
print(curr)
print(curr + timedelta(hours=10))
print(curr - timedelta(hours=10))
print(curr + timedelta(days=5, hours=10))

#时区转换
#我们可以通过utcnow()方法拿到UTC时间，再转换成任意时区的时间
# 拿到UTC时间，并强制设置时区为UTC+0:00:
# >>> utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# >>> print(utc_dt)
# 2015-05-18 09:05:12.377316+00:00
# # astimezone()将转换时区为北京时间:
# >>> bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
# >>> print(bj_dt)
# 2015-05-18 17:05:12.377316+08:00
# # astimezone()将转换时区为东京时间:
# >>> tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
# >>> print(tokyo_dt)
# 2015-05-18 18:05:12.377316+09:00
# # astimezone()将bj_dt转换时区为东京时间:
# >>> tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
# >>> print(tokyo_dt2)
# 2015-05-18 18:05:12.377316+09:00