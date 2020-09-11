# coding:utf-8
# 関数で可変個数の引数を受け取る
# 可変個数の引数を定義する
def myunc(category, *ranktuple):
    count = 1
    print(category)
    for val in ranktuple:
        print("No." + str(count) + ":" + val)
        count += 1
    print("\n",end=")

    myfunc("Fruits", "Orange", "Melon", "Banana", "Apple")
    myfunc("Mobile", "Android", "iPhone")