# coding:utf-8
# returnを使って戻り値を渡す
def myfunc(num):
    if num % 2 == 0:
        return "偶数です"
    return "奇数です"

for i in range(1, 10):
    print(str(i) + "は" + myfunc(i))



# 複数の値を戻り値として返す
def myfunc(num1, num2):
    goukei = num1 + num2
    heikin = (num1 + num2) / 2
    return (goukei,heikin)

num1 = 10
num2 = 8
x = myfunc(num1, num2)

print("num1 - " + str(num1))
print("num2 = " + str(num2))
print("合計 = " + str(x[0]))
print("平均 = " + str(x[1]))


