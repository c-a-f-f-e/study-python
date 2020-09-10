# coding:utf-8
# インデックスを相手いして要素を取得する
mytuple = ("Orange", "Lemon", "Apple")
print(mytuple[0])
print(mytuple[1])
print(mytuple[2])
# 負の値のインデックスでの指定
mytuple = ("Orange", "Lemon", "Apple")
print(mytuple[-1])
print(mytuple[-2])
print(mytuple[-3])

# タプルの最後の要素のインデックスを調べる
mytuple = ("Orange", "Lemon", "Apple")
print(len(mytuple))
# 最後の値の取得
mytuple = ("Orange", "Lemon", "Apple")
print(mytuple[len(mytuple)-1])


# サンプルプログラム
animaltuple = ("Cat", "Dog", "Cow", "Monky")

print(animaltuple)
print("最後の要素は" + animaltuple[0] + "です。")
print("最後の要素は" + animaltuple[len(animaltuple)-1] + "です。")
