# coding:utf-8
# 関数を呼び出すときに引数を使って値を渡す
# 引数を指定した関数の呼び出し　
def myfunc(str1, num1):
    print("Name: " + str1 + "Old: " + str(num1))

myfunc("Yamada", 28)
myfunc("Suzuki", 32)

def myfunc(mylist):# 仮引数
    print("Name: " + mylist[0] + ", Old:" + str(mylist[1]))

myfunc(["Yamada", 28])# 実引数
myfunc(["Suzuki", 34])
