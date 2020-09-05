# 基本的な使い方
print('python')
print('-')
print('izm')
print('com')


# end引数　デフォルトで＼nがある事に注意
print('python', end=' ')
print('-', end= ' ')
print('izm', end=' ')
print('com')


# file引数　file引数なしでprintを実行すると本の出力先(コンソール)へ出力される
f_obj = open('text.txt', 'w')

print('python-izm.zom', file=f_obj)


# フォーマット出力　%は文字列、%dは数値として認識される
print('Pythonの学習サイト : %s' % 'python-izm.com')
print('Pythonの学習サイト : %s-%s.%s' % ('python', 'izm', 'com'))

test_int = 100 + 100
test_str = 'python-izm.com'
print('サイト開設 %d 日目! %s' % (test_int, test_str))


# format
print('Pythonの学習サイト : {}'.format('python-izm.com'))
print('Pythonの学習サイト : [0]-[1].[2]'.format('python,', 'izm', 'com'))

test_int = 100 + 100
test_str = 'python-izm.com'
print('サイト開設 {1} 日目! {0}'.format(test_str, test_int))