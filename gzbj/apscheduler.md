# 定时框架APScheduler



> APSScheduler是python的一个定时任务框架，它提供了基于日期date、固定时间间隔interval、以及linux上的crontab类型的定时任务。该框架不仅可以添加、删除定时任务，还可以将任务存储到数据库中、实现任务的持久化。



## APScheduler有四种组件



- triggers（触发器）：触发器包含调度逻辑，每一个作业有它自己的触发器，用于决定接下来哪一个作业会运行，除了他们自己初始化配置外，触发器完全是无状态的。
- job stores（作业存储）：用来存储被调度的作业，默认的作业存储器是简单地把作业任务保存在内存中，其它作业存储器可以将任务作业保存到各种数据库中，支持MongoDB、Redis、SQLAlchemy存储方式。当对作业任务进行持久化存储的时候，作业的数据将被序列化，重新读取作业时在反序列化。
- executors（执行器）：执行器用来执行定时任务，只是将需要执行的任务放在新的线程或者线程池中运行。当作业任务完成时，执行器将会通知调度器。对于执行器，默认情况下选择ThreadPoolExecutor就可以了，但是如果涉及到一下特殊任务如比较消耗CPU的任务则可以选择ProcessPoolExecutor，当然根据根据实际需求可以同时使用两种执行器。
- schedulers（调度器）：调度器是将其它部分联系在一起，一般在应用程序中只有一个调度器，应用开发者不会直接操作触发器、任务存储以及执行器，相反调度器提供了处理的接口。通过调度器完成任务的存储以及执行器的配置操作，如可以添加。修改、移除任务作业



## APScheduler提供了七种调度器



- BlockingScheduler：适合于只在进程中运行单个任务的情况，通常在调度器是你唯一要运行的东西时使用，适用于只跑调度器的程序。
- BackgroundScheduler: 适合于要求任何在程序后台运行的情况，当希望调度器在应用后台执行时使用。适用于只跑调度器的程序。
- AsyncIOScheduler：适合于使用asyncio异步框架的情况
- GeventScheduler: 适合于使用gevent框架的情况
- TornadoScheduler: 适合于使用Tornado框架的应用
- TwistedScheduler: 适合使用Twisted框架的应用
- QtScheduler: 适合使用QT的情况



## APScheduler提供了四种存储方式



- MemoryJobStore
- sqlalchemy
- mongodb
- redis



## APScheduler提供了三种任务触发器



- data：固定日期触发器：任务只运行一次，运行完毕自动清除；若错过指定运行时间，任务不会被创建
- interval：时间间隔触发器
- cron：cron风格的任务触发





###  case1 :

#### 1.触发器date

特定的时间点触发，只执行一次。参数如下：



| 参数                              | 说明                 |
| --------------------------------- | -------------------- |
| run_date (datetime 或 str)        | 作业的运行日期或时间 |
| timezone (datetime.tzinfo 或 str) | 指定时区             |



使用例子：

```
from datetime import datetime
from datetime import date
from apscheduler.schedulers.blocking import BlockingScheduler

def job(text):    
    print(text)

scheduler = BlockingScheduler()
# 在 2019-8-30 运行一次 job 方法
scheduler.add_job(job, 'date', run_date=date(2019, 8, 30), args=['text1'])
# 在 2019-8-30 01:00:00 运行一次 job 方法
scheduler.add_job(job, 'date', run_date=datetime(2019, 8, 30, 1, 0, 0), args=['text2'])
# 在 2019-8-30 01:00:01 运行一次 job 方法
scheduler.add_job(job, 'date', run_date='2019-8-30 01:00:00', args=['text3'])

scheduler.start()
```



#### 2.触发器interval

| 参数                             | 说明       |
| -------------------------------- | ---------- |
| weeks (int)                      | 间隔几周   |
| days (int)                       | 间隔几天   |
| hours (int)                      | 间隔几小时 |
| minutes (int)                    | 间隔几分钟 |
| seconds (int)                    | 间隔多少秒 |
| start_date (datetime 或 str)     | 开始日期   |
| end_date (datetime 或 str)       | 结束日期   |
| timezone (datetime.tzinfo 或str) |            |





使用例子：

```
import time
from apscheduler.schedulers.blocking import BlockingScheduler

def job(text):    
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print('{} --- {}'.format(text, t))

scheduler = BlockingScheduler()
# 每隔 1分钟 运行一次 job 方法
scheduler.add_job(job, 'interval', minutes=1, args=['job1'])
# 在 2019-08-29 22:15:00至2019-08-29 22:17:00期间，每隔1分30秒 运行一次 job 方法
scheduler.add_job(job, 'interval', minutes=1, seconds = 30, start_date='2019-08-29 22:15:00', end_date='2019-08-29 22:17:00', args=['job2'])

scheduler.start()

'''
运行结果：
job2 --- 2019-08-29 22:15:00
job1 --- 2019-08-29 22:15:46
job2 --- 2019-08-29 22:16:30
job1 --- 2019-08-29 22:16:46
job1 --- 2019-08-29 22:17:46
...余下省略...
'''
```



#### 3.触发器cron

在特定时间周期性地触发。参数如下：



| 参数                             | 说明                                                         |
| -------------------------------- | ------------------------------------------------------------ |
| year (int 或 str)                | 年，4位数字                                                  |
| month (int 或 str)               | 月 (范围1-12)                                                |
| day (int 或 str)                 | 日 (范围1-31)                                                |
| week (int 或 str)                | 周 (范围1-53)                                                |
| day_of_week (int 或 str)         | 周内第几天或者星期几 (范围0-6 或者 mon,tue,wed,thu,fri,sat,sun) |
| hour (int 或 str)                | 时 (范围0-23)                                                |
| minute (int 或 str)              | 分 (范围0-59)                                                |
| second (int 或 str)              | 秒 (范围0-59)                                                |
| start_date (datetime 或 str)     | 最早开始日期(包含)                                           |
| end_date (datetime 或 str)       | 最晚结束时间(包含)                                           |
| timezone (datetime.tzinfo 或str) | 指定时区                                                     |



使用例子：

```
import time
from apscheduler.schedulers.blocking import BlockingScheduler

def job(text):    
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print('{} --- {}'.format(text, t))

scheduler = BlockingScheduler()
# 在每天22点，每隔 1分钟 运行一次 job 方法
scheduler.add_job(job, 'cron', hour=22, minute='*/1', args=['job1'])
# 在每天22和23点的25分，运行一次 job 方法
scheduler.add_job(job, 'cron', hour='22-23', minute='25', args=['job2'])

scheduler.start()

'''
运行结果：
job1 --- 2019-08-29 22:25:00
job2 --- 2019-08-29 22:25:00
job1 --- 2019-08-29 22:26:00
job1 --- 2019-08-29 22:27:00
...余下省略...
'''
```



#### 4.通过装饰器scheduled_job()添加方法

添加任务的方法有两种：

（1）通过调用add_job()---见上面1至3代码
（2）通过装饰器scheduled_job()：
第一种方法是最常用的方法。第二种方法主要是方便地声明在应用程序运行时不会更改的任务。该 add_job()方法返回一个apscheduler.job.Job实例，可以使用该实例稍后修改或删除该任务

| 表达式 | 参数类型 | 描述                                     |
| ------ | -------- | ---------------------------------------- |
| *      | 所有     | 通配符。例： minutes=* 即每分钟触发      |
| */a    | 所有     | 可被a整除的通配符。                      |
| a-b    | 所有     | 范围a-b触发                              |
| a-b/c  | 所有     | 范围a-b，且可被c整除时触发               |
| xth y  | 日       | 第几个星期几触发。x为第几个，y为星期几   |
| last x | 日       | 一个月中，最后个星期几触发               |
| last   | 日       | 一个月最后一天触发                       |
| x,y,z  | 所有     | 组合表达式，可以组合确定值或上方的表达式 |



```
import time
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

@scheduler.scheduled_job('interval', seconds=5)
def job1():
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print('job1 --- {}'.format(t))

@scheduler.scheduled_job('cron', second='*/10')
def job2():
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print('job2 --- {}'.format(t))

scheduler.start()
```

