# coding:utf-8
# タプルの要素を昇順または降順に並び替える
# 要素の並び替え
numtuple = (55, 78, 92, 82, 65)

newnumlist = sorted(numtuple)
newnumtuple = tuple(newnumlist)

print("Before:", numtuple)
print("After:", newnumtuple)

animaltuple = ("Dog", "Cat", "Bear", "Deer")

newanimallist = sorted(animaltuple)
newanimaltuple = tuple(newanimallist)

print("Before:", animaltuple)
print("After:", newanimaltuple)