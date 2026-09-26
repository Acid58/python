#传参方式:
# 1.位置传参:按照参数顺序
# 2.关键字传参:不需要按照顺序
# 3.混合传参:只能先使用位置传参,后使用关键字传参

#默认参数:在不传参时取默认实参
# def rectangle_area(l,w=6):
#     area = l * w
#     return area
# print(rectangle_area(5))#area=30

#不定长参数:*args
# def calc(*args,**kwargs):
#     """
#     计算最小值最大值
#     :param args: 不定长位置参数,即录入的数据
#     :param kwargs: 不定长关键字参数
#        round:保留几位小数
#        print:是否打印输出
#     :return:
#     """
#     min_date = min(args)
#     max_date = max(args)
#     print(type(args))
#
#     return min_date,max_date
# print(calc(10,20,30,40))
# print(calc(10,20,30,40,round=1,print=True))

#参数类型
#普通参数:数字,布尔,字符串,列表,元组,集合,字典
#特殊参数:函数
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def calc(a,b,oper):
    return oper(a,b)
result1 = calc(10,20,add)
result2 = calc(10,20,subtract)
print(result1)
print(result2)