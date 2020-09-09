# coding:utf-8
stafflist = [["Yamada", 25], ["Suzuki", 38], ["Tanaka", 28]]

for p in [0, 1, 2]:
    for m in [0, 1]:
        print("[" + str(p) + "][" + str(m) + "] = ", end='')
        print(stafflist[p][m])
