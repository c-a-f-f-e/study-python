# coding:utf-8
# リスト内包表記による多重ループの記述方法
mylist = [i for i in range(1, 6)]
print(mylist)

mylist = []
for i in range(1, 6):
    mylist.append(i)
    print(mylist)


# 2重ループ
mylist = []
for i in range(1, 4):
    for j in range(1, 3):
        mylist.append(i * 10 + j)
print(mylist)
# 内包表記
mylist = [i * 10 + j for i in range(1, 4) for j in range(1, 3)]
print(mylist)


# リスト内包型による二次元配列の記述法
mylist = []
for i in range(1, 4):
    sublist = []
    for j in range(1, 3):
        sublist.append(i * 10 + j)
    mylist.append(sublist)
print(mylist)
# リスト内包型による表記
mylist = [[i * j for j in range(1, 3)] for i in range(1, 4)]
print(mylist)


