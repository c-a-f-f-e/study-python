# coding:utf-8
# リスト内包表記の使い方
mylist = [i for i in range(1, 6)]
print(mylist)

mylist = [i * 10 for i in range(1, 6)]
print(mylist)

mylist = []
for i in range(1, 6):
    mylist.append(i * 10)

    print(mylist)


# 条件式を加えたリスト内包表記
mylist = [i for i in range(1, 20) if i % 3 == 0]
print(mylist)

mylist = []
for i in range(1, 20):
    if i % 3 == 0:
        mylist.append(i)
    print(mylist)
