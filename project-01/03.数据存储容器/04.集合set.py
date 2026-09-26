#无序,不可重复,可修改
s1 = {1, 2, 3}
s2 = {2,3,4}
s3 = {1,2,6}
s4 = {2,3,5}
# s3 = set()
#
# s1.add(4)#加入新元素
# s1.remove(1)#移除元素
# e = s1.pop(4)#随即删除并用e接受
# s1.clear#清空
# s1.difference(s2)#差集
# s1.union(s2)#并集
# s1.intersection(s2)#交集

#案例
# french_set.intersection(art_set)
# french_set & art_set
s = s1 & s2 & s3 & s4
print(s)

#集合推导式
set0 = {s for s in s1}
