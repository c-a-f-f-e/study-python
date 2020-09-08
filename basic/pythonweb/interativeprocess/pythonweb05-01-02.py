# coding:utf-8
mylist = ["Orange", "Peach", "Lemon"]
for val in mylist:
    print(val)

print("End")



mylist = ["Orange", "Peach", "Lemon", "Apple"]
print(mylist)
for val in mylist:
    print("value:" + val)

print("\n")

mydict = {"L":"Lemon", "O":"Orange", "G":"Grapes"}
print(mydict)
for mykey, myvalue in mydict.items():
    print("key:" + mykey + ",value:" + myvalue)



count = 0
mylist = ["Orange", "Peach", "Lemon", "Apple"]
print(mylist)
for val in mylist:
    print("value:" + val)
    count += 1
else:
    print("要素の数 = " + str(count))
