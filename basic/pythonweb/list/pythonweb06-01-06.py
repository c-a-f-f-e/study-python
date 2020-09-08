# coding:utf-8
mylist = ["Blue", "Red", "Green"]
print(mylist)
# "White"を追加
mylist.append("White")
print(mylist)
# "Blackを追加"
mylist.append("Black")
print(mylist)



# スライスによる要素の追加
kantoulist = ["Tokyo", "Kanagawa", "Chiba", "Gumma"]
print(kantoulist)
addlist = ["Saitama", "Ibaraki", "Tocighi"]
print(addlist)

kantoulist[len(kantoulist):len(kantoulist)] = addlist
print(kantoulist)



# リストに別の要素のリストを追加する
eastlist = ["Tokyo", "Kanagawa", "Chiba"]
print(eastlist)
westlist = ["Osaka", "Nagoya", "Fukuoka"]
eastlist.extend(westlist)
print(eastlist)



# リスト同士の結合による新しいリストの作成
redlist = ["Orange", "Strawberry"]
print(redlist)
yellowlist = ["lemon", "Banana", "Grapefruit"]
print(yellowlist)
# redlistとyekkolistを結合する
fruitlist = redlist + yellowlist
print = (fruitlist)



# リストの要素要素を指定回数繰り返す新しいリスト
baselist = ["Yes", "No"]
print(baselist)

datalist = baselist * 4
print(datalist)