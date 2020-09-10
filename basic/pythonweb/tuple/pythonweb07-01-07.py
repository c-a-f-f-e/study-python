# coding:utf-8
# 指定した値と同じ値を持つ要素が含まれているかの確認
mytuple = ("A", "B", "C", "D", "E")
print("B" in mytuple)
print("D" in mytuple)
print("G" in mytuple)


# 指定の値と同じ要素が何個タプルに含まれているかの確認
mytuple = ("A", "B", "A", "A", "C")
print(mytuple.count("A"))
print(mytuple.count("B"))
print(mytuple.count("D"))


# 指定の値と同じ値を持つ要素のインデックスを取得
mytuple = ("A", "B", "A", "A", "C")
print(mytuple.index("A"))
print(mytuple.index("B"))
print(mytuple.index("C"))