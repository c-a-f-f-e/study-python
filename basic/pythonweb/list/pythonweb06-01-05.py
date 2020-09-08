colorlist = ["Blue", "Red", "Green"]

print(colorlist)
print("オブジェクトの id = " + str(id(colorlist)))
print("\n")

colorlist[1] = "White"
print(colorlist)
print("オブジェクトの id = " + str(id(colorlist)))


colorlist = ["Blue", "Red", "Green", "White"]
print(colorilst)

colorlist[1:3] = ["Yellow", "Pink", "Black"]
print(clorlist)

colorlist[1:5:2] = ["Gold", "Silver"]
print(colorlist)