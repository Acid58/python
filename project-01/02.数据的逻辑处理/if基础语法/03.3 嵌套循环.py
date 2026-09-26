# print(x)默认为print(x,end="\n")  end="\n"指的是每次输入以\n结束

# 打印九九乘法表
# for x in range(1,10):
#     for y in range(1,10):
#         if y <= x:
#             if y == x:
#                 print(f"{y} * {x} = {x*y}")
#             else:
#                 print(f"{y} * {x} = {x*y}",end="\t")
#简化
# for x in range(1,10):
#     for y in range(1,x+1):
#         print(f"{y} * {x} = {x*y}",end="\t")
#     print()

#打印等腰直角三角形
# a = int(input("请输入等腰直角三角形的边长:"))
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print("*",end="\t")
#     print()

#打印数字金字塔
# num = int(input("请输入数字:"))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(j,end="\t")
#     print()

#打印国际象棋棋盘
for i in range(8):
    if i % 2 == 0:
        for j in range(4):
            print("□  ■", end="  ")
        print()
    else:
        for j in range(4):
            print("■  □", end="  ")
        print()