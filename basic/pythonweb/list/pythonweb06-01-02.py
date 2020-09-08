# coding:utf-8
# リストの値の取得
colorlist = ["Red", "Blue", "Green"]
print(colorlist[0])
print(colorlist[1])
print(colorlist[2])


# 負の値を用いての取得
colorlist = ["Red", "Blue", "Green"]
print(colorlist[-1])
print(colorlist[-2])
print(colorlist[-3])


# len関数
colorlist = ["Red", "Blue", "Green", "White", "Black"]

print(colorlist)
print("最初の要素は" + colorlist[0] + "です。")
print("最後の要素は" + colorlist[len(colorlist) -1] + "です。")
