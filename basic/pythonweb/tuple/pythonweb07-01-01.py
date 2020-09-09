# 値を指定してタプルを作成する
(7, 8, 6, 6, 9)
("Orange", "Lemon", "Apple")
(30, "Tokyo", "Suzuki", True)
("A", ("B", "C"), "D")
()
colortuple = ("White", "Black", "Reed")


# 変数に代入された値を要素として取得する
x = 9
y = 18
numtuple = (x, y)
print(numtuple)

numlist = (9, 18)
print(numlist)

x = 9
y = 18
numtuple = (x, y)
print(numtuple)
x = 20
print(numtuple)



# 要素を指定した個数繰り返すタプルを作成する
numtuple = (0,) * 10
print(numtuple)

numtuple = (10, 20, 30) * 3
print(numtuple)