# coding:utf-8
# 指定の値と同じものを持つ要素が含まれているかの確認
mylist = ["A", "B", "C", "D", "E"]
print("B" in mylist)
print("G" in mylist)


# 指定の値と同じ要素がリストに何個含まれているか取得
mylist = ["A", "B", "A", "A", "C"]
print(mylist.count("A"))
print(mylist.count("B"))
print(mylist.count("D"))

# 指定の値と同じ値を持つ要素のインデックスの取得
mylist = ["A", "B", "A", "A", "C"]
print(mylist.index("A"))
print(mylist.index("B"))
print(mylist.index("C"))