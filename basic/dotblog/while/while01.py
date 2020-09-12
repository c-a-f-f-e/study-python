# while文を使った繰り返し処理の基本
# while分による繰り返し処理
# while文の記述方法
from random import randrange
x = randrange(0, 10, 1)
while x <= 8:
    print(x)
    x = randrange(0, 10, 1)

# 直接while文にTrueを指定する脱げんループ
from random import randrange
x = randrange(0, 10, 1)
flag = True
while flag:
    print(x)
    break

# while文内でif文によってbreak文を発動させ無限ループを抜ける方法
from random import randrange
x = randrange(0, 10, 1)
flag = True
while flag:
    print(x)
    if x > 8:
        break
else:
    x = randrange(0, 10, 1)