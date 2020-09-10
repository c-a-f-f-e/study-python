# coding:utf-8
# 辞書から要素を削除
# del分を使って要素を削除
mydict = {"A":"Apple", "L":"Lemon", "O":"Orange"}
del mydict["L"]
print(mydict)


# 指定してキーの要素を削除
mydict = {"A":"Apple", "L":"Lemon", "O":"Orange"}
val = mydict.pop("L")
print(val)
print(mydict)


# 最後に追加された要素を取得した上で削除
mylist = {"A":"Apple", "L":"Lemon", "O":"Orange"}
val = mydict.popitem()
print(val)

print(mydict)

val = mydict.popitem()
print(val)
print(mydict)

val = mydict.popitem()
print(val)
print(mydict)