# dict = {"a": 1, "b": 2, "c": 3}
# print(dict["a"])
# dict["d"] = 4 #添加
# dict.pop("d") #删除
# del dict["c"] #删除
# dict["a"] = 2 #修改
# dict[key]     #根据key获取value
# dict.get(key) #根据key获取value
# dict.keys()   #获取所有key
# dict.values() #获取所有value
# dict.items()  #获取所有键值对key:value
# for key, value in dict.items():
#     print(key, value,end=" ")


#购物车系统
dict = {}
print("""
    1.添加购物车
    2.修改购物车
    3.删除购物车
    4.查询购物车
    5.退出购物车""")

while True:
    num = int(input("请选择编号(1-5):"))
    match num:
        case 1:
            name = input("请输入要添加商品的名称:")
            price = int(input("请输入要添加商品的价格:"))
            count = int(input("请输入要添加商品的数量:"))
            if name not in dict:
                dict[name] = price, count
                print("添加成功")
            else:
                print("商品已存在")
        case 2:
            name = input("请输入要修改商品的名称")
            price = int(input("请输入要修改商品的价格:"))
            count = int(input("请输入要修改商品的数量:"))
            if name in dict:
                dict[name] = price, count
                print("修改成功")
            else:
                print("商品不存在")
        case 3:
            name = input("请输入要删除的商品:")
            if name in dict:
                del dict[name]
                print("删除成功")
            else:
                print("商品不存在")
        case 4:
            for name, (price, count) in dict.items():
                print(f"商品名称:{name},商品价格:{price},商品数量:{count}")
        case 5:
            break