# coding:utf-8
# リスト型の基本
# リスト型の作成方法
x = ['a', 'b', 'c', 'd']
print(type(x))
print(x)

# データ型の混在
x = [10, 10.5, False, 'a']
print(type(x))
print(x)

a = 'a'
b = 'b'
c = 'c'
d = 'd'
x = [a, b, c, d]
print(x)

# リストの中にリスト
x = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h']]
print(x)

x = ['a', 'b', 'c', 'd']
y = ['e', 'f', 'g', 'h']
z = [x, y]
print(z)

# 演算子を使ったlist型リストの操作
x = ['a', 'b', 'c', 'd']
y = ['e', 'f', 'g', 'h']
z = x + y
print(z)

# 演算子を使ったリストの繰り返し
x = ['a', 'b', 'c', 'd']
z = x * 3
print(z)

# 演算子の複合利用
x = ['a', 'b', 'c', 'd']
y = ['e', 'f', 'g', 'h']
z = x * 2 + y
print(z)

# +=によるリストの追加
x = []
x += ['a', 'b', 'c', 'd']
x += ['e', 'f', 'g', 'h']
print(x)

# 空リスト
x = []
print(type(x))
print(x)

x = ['a', 'b', 'c', 'd']
z = x * 0
print(type(0))
print(z)



# リストから部分的に値を取得する方法
# インデックスを使った方法
x = ['a', 'b', 'c', 'd']
z = x[1]
print(z)

x = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h']]
y = x[1][2]
y =x[1][2]
print(y)

x = ['a', 'b', 'c', 'd']
z = x[-1]
print(z)

# スライスを使った取得方法
x = ['a', 'b', 'c', 'd']
z = x[1:3]
print(z)

x = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h']]
y = x[1][2:4]
print(y)

x = ['a', 'b', 'c', 'd']
z = x[:3]
print(z)

x = ['a', 'b', 'c', 'd']
z = x[1:]
print(z)



# リストの変更と削除
x = ['a', 'b', 'c', 'd']
x[1] = 'z'
print(x)

x = ['a', 'b', 'c', 'd']
del x[1]
print(x)