# coding:utf-8
# 指定した値と同じ要素が含まれているかの確認
myset = {"A", "B", "C"}
"A" in myset
"D" in myset
# frozenset型
myfrozenset = frozenset(["A", "B", "C"])
"A" in myfrozenset
"D" in myfrozenset
