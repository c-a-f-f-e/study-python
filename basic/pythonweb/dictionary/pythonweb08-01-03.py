# coding:utf-8
# 辞書の値を変更/更新
# 辞書の要素の値の変更
mydict = {1:"Movie", 2:"Foods", 3:"Reading"}
mydict[2] = "Sports"
print(mydict)

# 辞書に新しい値を追加する
mydict = {1:"Movie", 2:"Foods", 3:"Reading"}
mydict[4] = "Sports"
print(mydict)

# サンプルプログラム
mydict = {"w":"Water", "o":"Orange", "t":"Tea"}
print(mydict)

mydict["t"] = "GreenTea"
print(mydict)

mydict["c"] = "Coffee"
print(mydict)

# 他の辞書データを使って辞書の要素の値を更新したり新しい要素を追加
lunchdict = {"a":"curry", "b":"paster", "c":"udon"}
print(lunchdict)

todaydict = {"b":"ramen", "d":"omlette"}
lunchdict.update(todaydict)
print(lunchdict)
