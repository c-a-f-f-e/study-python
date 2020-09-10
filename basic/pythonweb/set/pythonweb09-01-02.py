# coding:utf-8
# いてラブルナオブジェクトの作成
myset = set("Hello Python")
print(myset)

myfrozenset = frozenset("HEllo Python")
print(myfrozenset)
# リストから集合を作成
mylist = ["A", "B", "C"]
myset = set(mylist)
print(mylist)

myfrozenset = frozenset(mylist)
print(myfrozenset)
frozenset(['B', 'C', 'A'])



# リストから集合を作成
mylist = ["A", "B", "C"]
myset = set(myset)
print(mylist)

myfrozenset = frozenset(mylist)
print(myfrozenset)



# タプルから集合を作成
mytuple = ("A", "B", "C")
myset = set(mytuple)
print(myset)

myfrozenset = frozenset(mytuple)
print(myfrozenset)



# rangeから集合を作成
mylist = set(range(10))
print(myset)

myfrozenset = frozenset(range(10))
print(myfrozenset)
