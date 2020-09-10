# coding:utf-8
# 集合への要素の追加と集合からの要素の削除
# 集合に要素を追加
colorset = {"Red", "Green", "Blue"}
colorset.add("White")
print(colorset)



# 集合から要素を削除
# romove
colorset = {"Red", "Green", "Blue"}
colorset.remove("Green")
print(colorset)
# discard
colorset = {"Red", "Green", "Blue"}
colorset.discard("Green")
print(colorset)
# pop
colorset = {"Red", "Green", "Blue"}
colorset.pop()
print(colorset)
colorset.pop()
print(colorset)



# 集合から全ての要素を削除
colorset = {"Red", "Green", "Blue"}
colorset.clear()
print(colorset)