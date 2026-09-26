# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(999))


def main(coupon,points,postage,*args):
    total = sum(item[1] * item[2] for item in args) + postage
    if total >= 3000:
        choice = input("1.优惠券 2.积分 请选择编号:")
        match choice:
            case "1":
                total = total * coupon
            case "2":
                if points//100 < total:
                    total = total - points//100
                    points = points - (points//100)
                elif points//100 >= total:
                    points = points - total * 100
                    total = 0
            case _:
                print("格式错误")
    return total
print(main(
    0.5,
    600000000,
    10,
    ("飞机杯", 100, 2),
    ("甲基吧", 100, 2),
))
