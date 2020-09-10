# coding:utf-8
# 辞書でキーを指定して値を取得
mydict = {"JP":"Japan", "DE":"Germany", "FR":"France"}
print(mydict["DE"])
print(mydict["FR"])
print(mydict["JP"])

mydict = {"JP":"Japan", "DE":"Germany", "FR":"France"}

print(mydict)
key1 = "JP"
print("キー:" + key1 + "、値:" + mydict[key1])
key2 = "FR"
print("キー:" + key2 + "、値:" + mydict[key2])


# getメソッドを使用いて値を取得する
mydict = {"JP":"Japan", "DE":"Germany", "FR":"France"}

print(mydict)
key1 = "JP"
print("キー:" + key1 + "、値:" + mydict.get(key1, "NotFound"))
key2 = "FR"
print("キー:" + key2 + "、値:" + mydict.get(key2, "NotFound"))
key3 = "EN"
print("キー:" + key3 + "、値:" + mydict.get(key3, "NotFound"))
