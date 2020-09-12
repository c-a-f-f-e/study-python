# coding:utf-8
# 比較演算子で条件の審議をチェックする
# ==
a = 10
b = 15
x = a == b
print(type(x))
print(x)

# !=
a = 10
b = 15
x = a != b
print(type(x))
print(x)

# <
a = 10
b = 15
x = a < b
print(type(x))
print(x)

# >
a = 10
b = 15
x = a > b
print(type(x))
print(x)

# <=
a = 10
b = 15
x = a <= b
print(type(x))
print(x)

# >=
a = 10
b = 15
x = a >= b
print(type(x))
print(x)



# 比較演算子を組み合わせて利用する
a = 10
b = 15
c = 15
x = a < b <= c
print(type(x))
print(x)



# 比較演算子を使った文字列の比較
a = 'A'
b = 'Z'
x = a == b
print(x)

a = 'A'
b = 'Z'
x = a < b
print(x)

a = 'ABC'
b = 'XYZ'
x = a != b
print(x)