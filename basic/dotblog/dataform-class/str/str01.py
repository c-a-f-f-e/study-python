# coding;utf-8
# str型の作成方法
x = 'テキスト'
print(x)
print(type(x))



# 複数のstr型作成方法
x = '''
<h1>タイトル</h1>
<a href="http://test.com/a.html">〇〇へリンク</a>
'''
print(x)

x = '''\
<h1>タイトル</h1>
<a href="http://test.com/a.html">〇〇へリンク</a>\
'''
print(x)



# 演算子を使った文字列の操作
link_url = 'http://test.com/a.html'
link_text = '００へリンク'
x = '<a href="' + link_url + '">' + link_text + '</a>'



# 演算子を使った文字列の繰り返し
link_url = 'http://test.com/a.html'
link_text1 = '◯'* 3
link_text2 = 'へリンク'
link_text3 = link_text1 + link_text2
x = '<a href="' + link_url + '">' + link_text3 + '</a>'
print(x)



# 演算子の複合利用
link_url = 'http://test.com/a.html'
link_text = '◯'* 3 + 'へリンク'
x = '<a href="' + link_url + '">' + link_text3 + '</a>'
print(x)



# +=による文字列の追加
x = ''
x += '<a href="'
x = 'http://test.com/a.html'
x = '◯' * 3
x += 'へリンク'
x += '</a>'
print(x)
print(type(x))


# 文字列を部分的に取り出す方法
# n文字目の取得
x = '吾輩は猫である'
n = 1
print(x[n])
print(x[n-1])



# n文字目からm文字目の文字の取得
x = '吾輩は猫である'
n = 1
m = 3
print(x[n-1:m])