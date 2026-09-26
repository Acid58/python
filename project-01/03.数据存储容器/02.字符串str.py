# s = "python"
# #索引
# print(s[1])
# print(s[-1])
#字符串切片与列表切片一样
#字符串不可修改

#案例
# mail = input("请输入您的邮箱:")
# if mail.count("@") == 1 and "." in mail:
#     print(f"")

# # 判断是否为回文
# a = input("请输入:")
# if a[::] == a[::-1]:
#     print("是")
# else:
#     print("否")

list = []
for i in range(10):
    x = input("请输入字符串:").upper()
    list.append(x)
list.reverse()
for item in list:
    print(item,end="")
