# coding:utf-8
# print関数の使い方
# print関数の書式と基本的な使い方
print("Hello")
print(256)
print("Blue", "Red", "Green")



# 区切り文字を変更する
print("Blue", "Red", "Green")
print("Blue", "Red", "Green", sep="+")
print("Blue", "Red", "Green", sep="")



# print関数を実行した時に改行されない様にする
print("Hello ", end="")
print("buzz, ", end="")
print("How are you?", end="[end]\n")



# ファイルへ出力する
myfile = open("output1_4.text", "w")
print("Hello", file=myfile)
print("Bye", file=myfile)
myfile.close()