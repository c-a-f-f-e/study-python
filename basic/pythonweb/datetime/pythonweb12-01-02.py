# coding:utf-8
# タイムゾーンのインスタンスの作成
# timezoneクラス
import datetime

tokyo_tz = datetime.timezone(datetime.timedelta(hours=9))
print(tokyo_tz)

ny_tz = datetime.timezone(datetime.timedelta(hours=-4))
print(ny_tz)
# UTCのタイムゾーンの取得
utc_tz1 = datetime.timezone(datetime.timedelta(0))
print(utc_tz1)

ny_tz2 = datetime.timezone.utc
print(utc_tz1)
# サンプルプログラム
import datetime
print(datetime.timezone(datetime.timedelta(hours=9)))
print(datetime.timezone(datetime.timedelta(hours=-4)))
print(datetime.timezone.utc)