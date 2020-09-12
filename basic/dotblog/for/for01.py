# coding:utf-8
# for文を使った繰り返し処理の基本
# for文の基本的な書き方
for var in ['Python', 'javascript', 'ruby']:
    print(var)

for var in ['Python', 'javascript', 'ruby']:
    print(var)
print(var)

# for分でlistを使った繰り返し処理
formulas = [1+1, 1+2, 1+3]
for formula in formulas:
    result = formula * 5
    print(result)

# for文でループの回数を指定
for x in range(3):
    print(x)
    