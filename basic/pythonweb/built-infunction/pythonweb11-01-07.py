# coding:utf-8
# instance関数及type関数の使い方
#type関数の書式と基本的な使い方
print(type("str"))
print(type(100))
print(type(14.5))
print(type(7.0 + 5j))
print(type([1, 2, 3]))
print(type((1, 2, 3)))
print(type({1:"A", 2:"B", 3:"C"}))
print(type(True))
print(type(None))
# もうひとつサンプルプログラム
mylist = [2, "ab", 3.5, True, 4]
total = 0

for val in mylist:
    if type(val) in (int, float):
        print("val:" + str(val))
        total += val

print("total:" + str(total))



# instance関数の使い方
mylist = [2, "ab", 3.5, True, 4]
total = 0

for val in mylist:
    if isinstance(val, (int, float)):
        print("val:" + str(val))
        total += val

print("total:" + str(total))
