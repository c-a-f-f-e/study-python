# coding:utf-8
# if分の基本をマスターして条件分岐を思い通りに

# if文の記述方法
set_number = 90
if set_number >= 80:
    print('おめでとう')

# else
set_number = 90
if set_number >= 80:
    print('おめでとう')
else:
    print('頑張りましょう')

# elif
set_number = 90
if set_number >= 80:
    print('おめでとう')
elif set_number >= 70 and set_number < 80:
    print('あと少し')
else:
    print('頑張りましょう')

# elifを使用する時の注意点
set_number = 90
if set_number >= 80:
    print('おめでとう')
elif set_number >= 70 and set_number < 80:
    print('あと少し')
elif set_number >= 75 and set_number < 80:
    print('おしい！')
else:
    print('頑張りましょう')

# ifの入れ子構造
set_sex = '男'
set_age = 38
if set_sex == '男':
    if set_age >= 20:
        print('性別男性：20歳以上')
    else:
        print('性別男性：20歳未満')
else:
    if set_age >= 20:
        print('性別女性：20歳以上')
    else:
        print('性別女性：20歳未満')