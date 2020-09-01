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

#数値と文字列の比較　　int関数(文字列の数値への変換)
import random
a = random.randint(0, 9)
print(a)

b = int(input("数を入れてね>"))
if a == b:
    print("当たり")
else:
    print("はずれ")