# coding:utf-8
numlist = [84, 75, 92, 78]

newnumlist = sorted(numlist)
print("Before:", numlist)
print("After:", newnumlist)


colorlist = ["Blue," "Red", "Green", "White", "Black"]

newcolorlist = sorted(colorlist)
print("Blue:", colorlist)
print("After:", newcolorlist)
print("After:", newcolorlist)


# 要素の値のデータ型が異なっていた場合
numlist = [5, 3, 3.14, 4.78, 4]
sorted(numlist)

mylist = ["80", 75, 45, "68"]
sorted(mylist)



# 並べ替えるときの昇順と降順を切り替える
colorlist = ["Blue", "Red", "Green", "White", "Black"]

upcolorlist = sorted(colorlist)
downcolorlist = sorted(colorlist, reverse=True)
print("Original:", colorlist)
print("ABC:", upcolorlist)
print("DESC:", downcolorlist)



# 要素の値を他の関数に渡して帰ってきた値を使って並び替える
animallist = ["Cat", "monky", "bear", "Sheep", "cow"]

sortlist = sorted(animallist)
lowersortlist = sorted(animallist, key=str.lower)
print(animallist)
print(sortlist)
print(lowersortlist)