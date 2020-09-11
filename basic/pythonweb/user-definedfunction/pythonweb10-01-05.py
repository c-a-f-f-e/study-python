# coding:utf-8
# 引数にデフォルト値を設定
def myfunc(msg = "Hello"):
    print(msg)

myfunc("こんにちは")
myfunc()




# 複数の引数にデフォルト値を設定する場合の注意
def myfunc(num1, str1 = "未入力", str2 = "不明"):
    print("年齢は" + str(num1) + "です。", end=")
    print("名前は"+ str1 + "です。", end=")
    print("住所は" + str2 + "です。")


myfunc(28, "Suzuki", "Tokyo")
myfunc(25, "Yamada")
myfunc(30)



# デフォルト値にリストなどのミュータブルオブジェクトを設定する時の注意点
def myfunc(str1, list1 =["a"]):
    list1.append(str1)
    return list1

myfunc("b")
myfunc("c")
myfunc("d")



# ミュータブルなオブジェクトを毎回初期化して利用したい場合
def myfunc(str1, list1  = None):
    if list1 is None:
        list1 = ["a"]
    list1.append(str1)
    return list1

myfunc("b")
myfunc("c")
myfunc("d")
