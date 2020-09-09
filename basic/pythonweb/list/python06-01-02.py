# coding:utf-8
# delを使って要素を削除する
fruitlist = ["Orange", "Lemon", "Peach", "Grapes", "Apples"]
print(fruitlist)

del fruitlist[2]
print(fruitlist)

del fruitlist[1:3]
print(fruitlist)


# スライス機能を使って要素を削除する
numlist = ["One", "Two", "Three", "Four", "Five"]
print(numlist)

numlist[2:3] = []
print(numlist)

numlist[1:3] = []
print(numlist)


# インデックスで指定した要素を削除する
fruitlist = ["Orange", "Lemom", "Peach", "Grapes", "Apple"]
print(fruitlist)

print("最後のリスト", fruitlist.pop(), "を削除")
print(fruitlist)

print("最後のリスト", fruitlist.pop(), "を削除")
print(fruitlist)

print("最後のリスト", fruitlist.pop(), "を削除")
print(fruitlist)


# 指定した値と同じ値を持つ要素を削除する
animallist = ["Dog", "Cat", "Monky", "Bear", "Rabbit"]
print(animallist)

animallist.remove("Monky")
print(animallist)

animallist.remove("Rabbit")
print(animallist)


# リストから全ての値を削除する
colorlist = ["Blue", "Red", "Green"]
print(colorlist)

colorlist.clear()
print(colorlist)