#Flag　準備の是非を判断する為に使われるTrueかFalseかを格納する変数
#準備が整ったら旗を上げ(True)、まだなら旗を下げる(False)ことに見立ててある
# coding:utf-8
import random

isok = False
while isoke == False:
    b = input("数を入れてね>")
    if len(b) != 4:
        print("4桁の数字を入れて下さい")
    else:
        isok = True

print(b[0])
print(b[1])
print(b[2])
print(b[3])
