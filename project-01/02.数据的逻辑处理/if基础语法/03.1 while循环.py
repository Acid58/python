#while
# i = 0
# while i<10:
#     print("hello world")
#     i+=1
# else:
#     print("循环结束")

# 累加1~100所有偶数
total = 0
i = 1
while i <=100 :
    if i % 2 == 0:
        total = total + i
    i = i + 1
print(total)

#关注的是循环的条件