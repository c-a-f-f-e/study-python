#coding=utf-8
#hit and blow

#randomモジュール
import random

a = random.randit(0, 9)
print(a)

#input 関数
b = input("数を入れてね>")
print(b)

#あたりかどうかの判別
if a == b:
    print("当たり")
else:
    print("はずれ")
