# coding:utf-8
# Pythonでの正規表現の利用
# パターンの定義
import re
pattern = re.compile(r'a...e')


# 文章とパターンがマッチするかどうか調べる
import re
target = 'I like apples and oranges'

ptn = re.compile(r'a...e')
result = ptn.search(target)
if result :
    print(result.group())