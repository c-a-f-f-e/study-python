# coding:utf-8
# 変数に代入された値をリストの要素として利用
x = 10
y = 15
numlist = [x, y]
print(numlist)


# 上記のプログラムと同じ
numlist = [10, 15]
print(numlist)


# リスト作成後に変更された変数の値はリストの要素には反映されない
x = 10
y = 15
numlist = [x, y]
print(numlist)
x = 50
print(numlist)


# 同じ要素を複数個もつリストの作り方
numlist = [0] * 10
print(numlist)


# 文字列バージョン
namelist = ["undefined"] * 5
print(namelist)


"""
なお繰り返す要素に他のリストを指定した場合、
リストを持つ要素を指定した個数持つ新しいリストを作成するのではなく、
リストに含まれる要素を指定した個数分繰り返した新しいリストを作成します。
"""
numlist = [10, 20, 30] * 3
print(numlist)