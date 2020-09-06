# クラスの基礎
class TestClass:
    def __init__(self, code, name):#クラスの初期化
        self.code = code
        self.name = name

    
classes = []
classes.append(TestClass(1, 'テスト1'))# クラスの利用
classes.append(TestClass(2, 'テスト2'))# クラスの利用

for test_cls in classes:
    print('==== Class ====')
    print('code --> ' + str(test_cls.code))
    print('name --> ' + test_cls.name)
