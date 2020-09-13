# coding:utf-8
# 関数の基本・関数作成時の書き方や利用方法
# 関数を使用しなかった場合
x1 = 'たろう'
y1 = 0
for i in x1:
    y1 += 1
print(y1)
x2 = 'さぶろう'
y2 = 0
for i in x2:
    y2 = 0
for i in x2:
    y2 += 1
print(y2)
x3 = 'ごろう'
y3 = 0
for i in x3:
    y3 += 1
print(y3)

# 使用した場合
def text_len(text):
    length = 0
    for i in text:
        length += 1
    return length

x1 = 'たろう'
print(text_len(x1))
x2 = 'さぶろう'
print(text_len(x2))
x3 = 'ごろう'
print(text_len(x3))


# 仮引数と実引数
def test(a):
    print(a)
test(5)

# デフォルト値を設定しない場合
def test(a, b, c):
    print(a)
    print(b)
    print(c)

# デフォルト値を設定する場合
def test(a=0, b=1, c=2):
    print(a)
    print(b)
    print(c)

# 仮引数がデフォルト値を持つ場合は関数実行時に実引数を省略できる
def test(a=0, b=1, c=2):
    print(a)
    print(b)
    print(c)

print(test())

# 実引数の「位置引数」と「キーワード引数」
# 位置引数
def test(a, b, c):
    print(a)
    print(b)
    print(c)
test(5, 10, 15)


# キーワード引数
def test(a, b, c):
    print(a)
    print(b)
    print(c)
test(c=15, a=5, b=10)


# 戻り値
def test(a, b, c, d=20, e=25):
    set_sum = a+b+c+d+e
    return set_sum
y = test(4, 10, 15, d=30, e=40)
print(y)

# 戻り値に指定できる形式
# リスト式
def test(a, b, c, d=20, e=25):
    set_list = [a, b, c, d, e]
    return set_list
y = test(4, 10, 15, d=30, e=40)
print(y)

# 辞書式
def test('a':a, 'b':b, 'c':c, 'd'd=20, 'e'e=25):
    set_dict = [a, b, c, d, e]
    return set_dict
y = test(4, 10, 15, d=30, e=40)
print(y)

#関数内で利用する変数名について
def test(a, b, c, d=20, e=25):
    set_sum = a+b+c+d+e
    return set_sum

# 関数内でグローバル変数「set_sum」を参照
set_sum = 300

def test(a, b, c, d=20, e=25):
    print(set_sum)

test(4, 10, 15, d=30, e=40)

# 関数内でグローバル変数「set_sum」に代入
set_sum = 300

def test(a, b, c, d=20, e=25):
    global set_sum
    print(set_sum)
    set_sum = a+b+c+d+e
    return set_sum

y = test(4, 10, 15, d=30, e=40)
print(y)
print(set_sum)