# coding:utf-8
#range関数の使い方
# range関数の書式と基本的な使い方
r = range(0, 10)
print(r)
print(list(r))
# インデックスの指定による要素の取得
r = range(0, 10)
print(r[0])
print(r[5])
print(r[3:7])
# サンプルプログラム
r = range(10)
for i in r: 
    print("num : " + str(i))