# 可変長引数
# *args
def test_func(*args):
    print(args)

test_func(1, 2, 3, 4, 5,)

# パスの結合
def test_func(code, name, *args):
    print(code, name)
    print(args)

test_func(100, 'python-izm', 'JP', 'US')


# 引数名は必ずしもargである必要はない
def test_func(**kwargs):
    print(kwargs)

test_func(code=100, name='python-izm')


# 引数名の前に**でも可変長引数が出来る
def test_func(**kwargs):
    print(kwargs)
test_func(code=100, name='python-izm')


# **の可変長引数は関数内においてディクショナリとなる
def test_func(code, name, kana, *args, **kwargs):
    print(code, name, kana)
    print(args)
    print(kwargs)

test_func(
    100, 'python-izm', u'パイソンイズム'
    'JP', 'US',
    email = 'xxx', city = 'Tokyo'
)