# coding:utf-8
# 論理演算子で複雑な条件判定方法
# or
a = 10
b = 15
c = 12
x = a > b or a != c
print(x)

# and
a = 10
b = 15
c = 12
x = a > b and a != c
print(x)

# not
a = 10
b = 15
c = 12
x = not a > b
print(x)



# 組み合わせた論理演算子の優先順位と条件判定
a = 5
b = 15
c = 30
d = 5
x = a < b or a >= c and not a == d
print(x)

# ()を使って優先順位を変更
a = 5
b = 15
c = 30
d = 5
x = (a < b or a >= c) and not a == d
print(x)