#break 结束循环
#continue 结束当前循环,进入下次循环
from functools import total_ordering

# 登录系统
while True:
     username = input("请输入用户名:")
     password = input("请输入密码:")

     if username == "" and password == "":
         print("用户名和密码不能为空")
         continue

     if username == "1" and password == "1":
         print("登录成功")
         break
     elif username == "2" and password == "2":
         print("登录成功")
         break
     elif username == "3" and password == "3":
         print("登录成功")
         break
     else:
         print("账号或密码错误,请重新输入")

#猜数字游戏
#生成随机数
# import random
# random_number = random.randint(1,100)
# while True:
#     num = float(input("请输入数字:"))
#     if num == random_number:
#         print("正确")
#         break
#     elif num > random_number:
#         print("偏大")
#         continue
#     elif num < random_number:
#         print("偏小")

# #1-1000所有5的倍数之和
# total = 0
# for i in range(1,1001):
#     if i % 5 == 0:
#         total += i
# print(total)
