- from datetime import datetime
  - datetime模块中包含了一个datetime类，如果只import datetime,就要用全称datetime.datetime调用方法。
  - 指定日期直接用datetime构造，dt = datetime.datetime(2016,04,15,12,20)

- datetime转timestamp
  - 我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数）.
  - dt.timestamp = 1460694000.0 秒数，小数点后表示毫秒，timestamp数值与时区无关，timestamp确定的是UTC+0:00时间。
  
- timestamp转换为datetime
  - timestamp没有时区概念，用fromtimestamp()方法是转换到当前时区的datetime。
  - 用utcfromtimestamp()方法转换到UTC+0:00时间。
  
- str转datetime
  - datetime.strptime('2016-04-15 12:20:00','%Y-%m-%d %H:%M:%S')
  
- datetime转换为str
```python
from datetime import datetime
dt = datetime.now()
print(dt.strftime(%a %b %H:%M:%S)
#值为Mon, May 05 16:28
```

- datetime加减
  - 加减可以直接用+和-运算符，不过需要导入timedelta这个类，from datetime import timedelta,datetime
  - datetime.now()+timedlta(days=1,hours=10)
 
***datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。***

***如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。***
