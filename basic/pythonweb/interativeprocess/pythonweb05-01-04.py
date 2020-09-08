# coding:utf-8
num = 0
while True:
    print("num = " + str(num))
    num += 1
    if num >= 2:
        break

print("End")



print("Start")

while True:
    print("数値を入力すると5倍した値を表示します")
    print("終了する場合は-1を入力して下さい")
    num = int(input("> "))
    if num == -1:
        break
    print("num = " + str(num) + ",num * =" + str(num * 5) + "\n")

print("End")



for val in [3, "ab", 7]:
    if isinstance(val,str):
        continue
    print("val = " + str(val))

print("End")



print("Start")
total = 0

for num in [35, 25, "OK", 45, "Pass", 28]:
    if isinstance(num, str):
        continue
    print("num = " + str(num))
    total += num

print("Total = " + str(total))
print("End")