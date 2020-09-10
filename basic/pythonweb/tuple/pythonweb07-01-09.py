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


# 要素の値を他の関数に渡して帰ってきた値を使って並び替える
mytuple = ("C", "b", "A", "E", "d")

sorttuple = tuple(sorted(mytuple))
lowersorttuple = tuple(sorted(mytuple, key=str.lower))

print(mytuple)
print(sorttuple)
print(lowersorttuple)