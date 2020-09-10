# coding:utf-8
# タプルでスライス機能を取得する
animaltuple = ("Cat", "Lion", "Cow", "Dog", "Girafe")

print(animaltuple)
print(animaltuple[1:4])
print(animaltuple[0:2])
print(animaltuple[2:3])


# 開始インデックスまたは終了インデックスの省略
animaltuple = ("Cat", "Lion", "Cow", "Dog", "Girafe")

print(animaltuple)
print(animaltuple[:3])
print(animaltuple[2:])
print(animaltuple[:])