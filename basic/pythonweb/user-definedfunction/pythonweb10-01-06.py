# coding:utf-8
# キーワード引数を使って関数を呼び出す
# 位置引数とキーワード引数
def myfunc(num1, str1):
    print("num1=" + str(num1))
    print("str1=" + str1)

myfunc(num1 = 10, str1 = "Orange")
str1 = 10
myfunc(str1 = "Lemon", num1 = 15)

# 位置引数とキーワード引数を混在させる
def myfunc(old, name, adress):
    print("年齢は" + str(old) + "です。",end="")
    print("名前は" + name "です。",end="")
    print("住所は" + adress + "です。")

myfunc(28, "Suzuki", "Tokyo")
myunc(adress="Osaka", old=25, name="Yamada")
myunc(32, adress="Kyoto", name="Honda")

