# coding:utf-8
# 辞書に含まれる全てのキーの取得
mydict = {"L":"Lemon", "O":"Orange", "G":"Grapes"}
print(mydict.keys())
# for文との組み合わせ
mydict = {"L":"Lemon", "O":"Orange", "G":"Grapes"}
for mykey in mydict.keys():
    print(mydict)
# リスト方のコントラクタの引数に指定することでキーの一覧をリストとして取得
mydict = {"L":"Lemon", "O":"Orange", "G":"Grapes"}
mylist = list(mydict.keys())
print(mylist)



# 辞書に含まれる全ての値を取得
mydict = {"L":"Lemon", "O":"Orange", "G":"Grapes"}
print(mydict.values())
# for文との組み合わせ
mydict = {"L":"Lemon", "O":"Orange", "G":"Grapes"}
for myvalue in mydict.values():
    print(myvalue)
# リスト方のコントラクタの引数に指定することでキーの一覧をリストとして取得
mydict = {"L":"Lemon", "O":"Orange", "G":"Grapes"}
mylist = list(mydict.values())
print(mylist)



# 辞書に含まれる全てのキーと値の組み合わせを取得
ydict = {"L":"Lemon", "O":"Orange", "G":"Grapes"}
print(mydict.items())
# for文との組み合わせ
mydict = {"L":"Lemon", "O":"Orange", "G":"Grapes"}
for mykey,myvalue in mydict.items():
    print("key:" + mykey + ", values:" + myvalue)
# リスト方のコントラクタの引数に指定することでキーの一覧をリストとして取得
mydict = {"L":"Lemon", "O":"Orange", "G":"Grapes"}
mylist = list(mydict.items())
print(mylist)