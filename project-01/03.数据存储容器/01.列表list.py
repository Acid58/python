s = [10,65,352,652,89]
# print(type(s))
# #获取
# print(s[0])
# print(s[-1])
# #修改
# s[0] = 50
# print(s[0])
# #删除
# del s[0]
# print(s[0])
# #遍历
# for item in s:
#     print(item)
# #切片
# s[0:2:1]
# print(s[:2:1])
# print(s[:2:1])
# s[-1:-3:1]
# print(s[0:-3:1])

#方法
# s.append(100)# 在尾部追加元素100
# s.insert(0,653)# 在第零个元素前穿插元素653
# s.remove(65)# 移除列表中第一个65
# s.pop(0)# 删除指定索引位置的元素,未指定则默认删除最后一个
# s.sort()# 对列表元素进行排序
s.sort(key=lambda item:len(item),reverse=False)#按照字符个数排序,False是从小到大
#s.reverse()#反转列表元素

#案例:将用户输入的10个数字存储到列表中,并排序,输出最小值,最大值,平均值
#sum求和函数,len表示元素数量
# num_list = []
# for i in range(10):
#     num = float(input("请输入一个有效数字:"))
#     num_list.append(num)
# num_list.sort()
# print(num_list)
# print(f"最小值为{num_list[0]},最大值为{num_list[9]},平均值为{sum(num_list)/len(num_list)}")

#合并两个列表,去除重复元素

# for num in num_list1:
#     if num not in num_list2:
#         num_list2.append(num)
# print(num_list2)

# new_list = []
# #num_list = [*num_list1,*num_list2]
# num_list = num_list1 + num_list2#*解包
# for num in num_list:
#     if num not in new_list:
#         new_list.append(num)
# print(new_list)

#生成1-20的平方列表

# num_list = []
# for i in range(1,21):
#     num_list.append(i**2)
# print(num_list)

#列表推导式
# num_list = [i**2 for i in range(1,20) if 条件]
# print(num_list)

#从一个数字列表中提取所有偶数,并平方,组成新列表
# num_list = [9,5,2,6,9,1,3,4,1,7,8,5,6]
# new_list = [i**2 for i in num_list if i%2==0]
# print(new_list)

# list = []
# list1 = [5,6,2,4,8,6]
# list2 = [3,9,7,1,4,26]
# list3 = [1,5,6,7,4]
# list4 = list1 + list2 + list3
# for i  in list4:
#     if i not in list:
#         list.append(i)
# print(list)

# list1 = [*range(1,10)]
# list = [i**2 for i in list1 if i % 3==0 or i % 5==0]
# print(list)

list1 = [*range(-11,10)]
list = [i for i in list1 if i < 0]
print(list)