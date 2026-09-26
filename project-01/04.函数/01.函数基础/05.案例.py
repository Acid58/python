#三角形面积
# def triangle_area(a,h):
#     """
#     计算面积
#     :param a:底
#     :param h:高
#     :return:面积
#     """
#     area = a * h / 2
#     return area
# a,h = float(input("请输入三角形的底:")),float(input("请输入三角形的高:"))
# print(triangle_area(a,h))


#计算字符串中元音字母的个数
# def letter_num(a):
#     num = 0
#     for i in a:
#         i = i.upper()
#         if i == "A":
#             num += 1
#         elif i == "E":
#             num += 1
#         elif i == "I":
#             num += 1
#         elif i == "O":
#             num += 1
#         elif i == "U":
#             num += 1
#     return num
# a = input("请输入字符串:")
# print(letter_num(a))


def class_score(score_list):
    max_s = max(score_list)
    min_s = min(score_list)
    avg = round(sum(score_list)/len(score_list),1)
    return max_s,min_s,avg
score_list = [1,2,3,4,5,6,7,8,9,10]
max_s,min_s,avg = class_score(score_list)
print(f"最高分:{max_s}")
