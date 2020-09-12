# coding:utf-8
# データ方の判別
x = 10
print(type(x))

x = 10.5
print(type(x))

x = "テキスト"
print(type(x))

x = "1"
print(type(x))

x = True
print(type(x))

x = [10, 20, 30, "テキスト"]
print(type(x))

x = (10, 20, 30, "テキスト")
print(type(x))

x = {'a':10, 'b':20, 'c':30, 'd':'テキスト'}
print(type(x))

# pythonのデータ方は動的型付け
x = 10
x = 10.5
print(type)

# 各データ方がある意味と専用ツール「メソッド」
# 同じデータ型同士の変数でなければ行えないこと
a = 10
print(a)
b = '10'
print(b)
print(type(a))
print(type(b))

# 各データ型による扱い方の違い
x = [10, 20, 30, 'テキスト']
y = x[1]
print(y)

x = {'a':10, 'b':20, 'c':30, 'd':'テキスト'}
y = x['c']
print(y)

x = 'abc'
y = x.upper()
print(y)