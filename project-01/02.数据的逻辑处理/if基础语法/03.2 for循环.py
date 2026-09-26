# msg = "Hello World"
# for item in msg:
#     print(item)
# else:
#     print("循环结束")

# msg = input("请输入需要遍历的字符串:")
# for i in msg:
#     print("元素:",i)
# else:
#     print("遍历结束")

#场景:关注的是遍历每一元素

#range
#range(end) 从0到end-1
#range(start,end) 从start到end-1
#range(start,end,step) step步长

#计算1~100所有奇数之和
# total = 0

# for i in range(1,101):
#     if i % 2 != 0:
#         total += 1
#
# for i in range(1,101,2):
#     total += i
#
# print(total)

#计算100-500所有3的倍数之和
total = 0
for i in range(100,501):
    if i % 3 == 0:
        total += i
print(total)