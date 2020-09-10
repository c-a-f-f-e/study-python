# coding:utf-8
# Pythonの引数における参照私と値私について
# 引数にイミュータブルなp部ジェクトを指定した場合
def myfunc(n):
    print(id(n))

x = 10
print(id(x))
myfunc(x)
# 別の例
def myfunc(n):
    print(n)
    n += 3
    print(n)

x = 10
print(x)
myfunc(x)
print(x)
# 引数にミュータブルなオブジェクトを指定した場合
def myfunc(n):
    print(id(n))

x = [10, 20]
print(id(x))
myfunc(x)
# 別の例
def myfunc(n):
    print(n)

x = [10, 20]
print(x)
myfunc(x)
print(x)