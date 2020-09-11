# coding:utf-8
# 四則演算

# 加算
x = 10 + 20
print(x)

# 減算
x = 10 -20
print(x)

# 乗算
x = 10 * 20
print(x)
x = -10 * 20
print(x)

# べき乗
x = 10 ** 3
print(x)

# 除算
x = 10 / 3 
print(x)

# 除算(小数点以下切り捨て)
x = 10 // 3
print(x)
x = 10 % 3
print(x)

# divmod関数
x = divmod(10, 3)
print(x)

# 数値演算子の優先順位
x = 10 + 5 * 2
print(x)

# カッコによる優先順位の変更
x = (10 + 5) * 2
print(x)

# 別パターン
x = ((3 + -10) * 20 - 10) ** 2
print(x)