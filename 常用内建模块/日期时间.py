#datetime 是Python处理日期和时间的标准库
from datetime import datetime
import time
for i in range(100):
    now = datetime.now()
    print(now)
    time.sleep(1)

#要获取指定时间，我们直接用参数构造一个datetime
