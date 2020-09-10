# coding:utf-8
# 集合と他の集合との関係を調べる
# 等しいかどうか
set1 = {"A", "B", "C"}
set2 = {"B", "C", "A"}
set1 ==  set2
# setとfrozensetとの比較も可能
set1 = {"A", "B", "C"}
set2 = frozenset(["B", "C", "A"])
set1 == set2



# 集合が他の集合と互いに素かどうか
set1 = {"A", "B"}
set2 = {"B", "D", "C", "A"}
set3 = {"B", "A"}
set1 <= set2
set2 <= set1
set1 <= set3
# issubset
set1 = {"A", "B"}
set2 = {"B", "D", "C", "A"}
set3 = {"A", "B"}
set1.issubset(set2)
set2.issubset(set1)
set1.issubset(set3)



# 集合が集合の真超集合かどうか
set1 = {"A", "B"}
set2 = {"B", "D", "C", "A"}
set3 = {"A", "B"}
set1 > set2
set2 > set1
set1 > set3



# 集合が他の集合と互いに素かどうか
set1 = {"A", "B"}
set2 = {"C", "D", "E"}
set3 = {"A", "C"}
set1.isdisjoint(set2)
set2.isdisjoint(set3)
set2.isdisjoint(set3)
