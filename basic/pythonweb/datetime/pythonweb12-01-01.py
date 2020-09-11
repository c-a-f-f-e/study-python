# coding:utf-8
# 日時と自国の情報をいていしてインスタンスを作成する
# datetimeクラス
import datetime

dt1 = datetime.datetime(2020,7,21)
print(dt1)

dt2 = datetime.datetime(2020,7,21,6,12,30,551)
print(dt2)

tokyo_tz = datetime.timezone(datetime.timedelta(hours=9))
dt3 = datetime.datetime(20,7,21,6,12,30,551,tokyo_tz)
print(dt3)



# dateクラス
import datetime
d = datetime.date(2020,7,21)
print(d)



# timeクラス
import datetime

t1 = datetime.time(6,12,30,551)
print(t1)

tokyo_tz = datetime.timezone(datetime.timedelta(hours=9))
t2 = datetime.time(6,12,30,551,tokyo_tz)
print(t2)



# サンプルプログラム
import datetime

print(datetime.datetime(20,7,21,6,12,30,551))
print(datetime.datetime(2019,12,9))
print(datetime.time(23,18,45,31112))

tokyo_tz = datetime.timezone(datetime.timedelta(hours=9))
print(datetime.datetime(2020,7,21,6,12,30,551,tokyo_tz))

ny_tz = datetime.timezone(datetime.timedelta(hours=-4))
print(datetime.datetime(2020,7,21,6,12,30,551,ny_tz))