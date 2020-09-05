# coding:utf-8
#各桁が数字であることの確認

import = random

isok = False
while isok == False:
    b = input("数字を入れてね")
    if len(b) != 4:
        print("四桁の数字を入れて下さい")
    else:
        if (b[0] < "0") or (b[1] > "9") :
            print("数字ではありません")
        elif (b[1] < "0") or (b[1] > "9") :
            print("数字ではありません")
        elif (b[2] < "0") or (b[2) > "9") :
            print("数字ではありせん")
        elif (b[3] < "0") or (b[3] > "9") :
            print("数字ではありません")
        else:
            isok = True

print(b[0])
print(b[1])
print(b[2])
print(b[3])
