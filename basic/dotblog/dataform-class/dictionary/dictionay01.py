# coding:utf-8
# 辞書の作成方法
x = {'A':'a', 'B':'b', 'C':'c', 'D':'d'}
print(type(x))
print(x)

# 作成時の注意点
x = {'A':'a', 'B':'b', 'C':'c', 'D':'d'}
print(x)

# キーの重複はNG
x = {'A':'a', 'A':'b', 'C':'c', 'D':'d'}
print(type(x))
print(x)

# データは混ぜても構成できる
x = {'A':10, 'B':10.5, 'C':False, 'D':'a'}
print(type(x))
print(x)

# 辞書の中にリストを含めることができる
x = {'A':[95, 68, 76, 98, 82], 'B':[86, 72, 91, 88, 73], 'C':[76, 77, 89, 99, 71]}
print(type(x))
print(x)

# 変数から辞書を作成する
a_key = 'A'
a_value = [95, 68, 76, 98, 82]
b_key = 'B'
b_value = [86, 72, 91, 88, 73]
c_key = 'C'
c_value = [76, 77, 89, 99, 71]
x = {a_key:a_value, b_key:b_value, c_key:c_value}
print(type(x))
print(x)


# 辞書のキーを使った要素の取得、追加、変更、削除方法
x = x = {'A':'a', 'B':'b', 'C':'c', 'D':'d'}
z = x['B']
print(z)

# キーを使った要素の追加
x = {'A':'a', 'B':'b', 'C':'c', 'D':'d'}
x['Z'] = 'z'
print(x)

# キーを使った要素の変更
x = {'A':'a', 'B':'b', 'C':'c', 'D':'d'}
x['B'] = 'z'
print(x)

# キーの使いどころ
x = {'A':'a', 'B':'b', 'C':'c', 'D':'d'}
del x['B']
print(x)