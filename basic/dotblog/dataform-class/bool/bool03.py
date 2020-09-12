# coding:utf-8
# in演算子で文字列やリスト内に含まれているか判定
# in演算子を使った条件の真偽取得
a = 'python code example'
x = 'python' in a
print(x)

a = 'python code example'
x = 'PYTHON' in a
print(x)

# in演算子を使ってリスト内に判定条件となる値が福間rているかを条件判断
a = [95, 68, 76, 98, 82]
x = 95 in a
print(x)

a = [95, 68, 76, 98, 82]
x = 95.0 in a
print(x)



# not in演算子を使った条件の真偽値取得
a = [95, 68, 76, 98, 82]
x = 95 not in a
print(x)
