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

#5-3   4桁のランダムな数字を作る str関数(数値の文字列への変換)
import random

a1 = random.randient(0, 9)
a2 = random.randient(0, 9)
a3 = random.randient(0, 9)
a4 = random.randient(0, 9)

print(str(a1) + str(a2) +  str(a3) + str(a4))

#リスト,要素,添字
a = [random.randient(0, 9),
    random.randient(0, 9),
    random.randient(0, 9),
    random.randient(0, 9)]
print(str(a[0]) + str(a[1]) + str(a[2]) + str(a[3]))

#5-4  入力を間違えた時にエラーを判別するために
