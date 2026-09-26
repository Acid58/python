# score = float(input("您的高考成绩:"))
# if score > 610: #记得写冒号,缩进
#     print("""
#     欢迎你来到石大读书
#     恭喜你踏入精彩的大学生活""")

# ok_account,ok_password = 123456,123456
# account,password= int(input("请输入账号:")),int(input("请输入密码:"))
# if account == ok_account and password == ok_password:
#     print("登录成功")
# if account != ok_account or password != ok_password:
#     print("账号或密码错误")

# ok_account,ok_password = 123456,123456
# account,password= int(input("请输入账号:")),int(input("请输入密码:"))
# if account == ok_account and password == ok_password:
#     print("登录成功")
# else:
#     print("账号或密码错误")

# num = float(input("请输入数字"))
# if num > 0:
#     print("正数")
# elif num < 0:
#     print("负数")
# else:
#     print("0")

# account1,account2,account3 = 1,2,3
# password1,password2,password3 = 1,2,3
# account,password = int(input("请输入账号:")),int(input("请输入密码:"))
# if account == account1 and password == password1 or account == account2 and password == password2 or account == account3 and password == password3:
#     print("登录成功")
# else:
#     print("账号或密码错误")

# score = float(input("总金额:"))
# if score >= 500:
#     print(f"应付金额为{score*0.8}")
# elif 300 <= score < 500:
#     print(f"应付金额为{score*0.9}")
# elif 100 <= score < 300:
#     print(f"应付金额为{score*0.95}")
# else:
#     print(f"应付金额为{score}")

# 判断三角形类型:等边 等腰 普通 不能构成
x,y,z = float(input("请输入边长x:")),float(input("请输入边长y:")),float(input("请输入边长z:"))
if x + y <= z or x + z <= y or y + z <= x:
    print("不能构成三角形")
elif x == y == z:
    print("等边三角形")
elif x == y != z or x == z != y or y == z != x:
    print("等腰三角形")
else:
    print("普通三角形")