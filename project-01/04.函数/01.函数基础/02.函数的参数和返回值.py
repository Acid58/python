def circle_area_len(r):
    area = 3.14 * (r ** 2)
    len =round(2 * 3.14 * r,1)
    return area,len
r = float(input("请输入半径:"))
al = circle_area_len(r)
print(al)


def rectangle_area(l,w):
    area = l * w
    return area
l,w = float(input("请输入长度:")),float(input("请输入宽度:"))
r_area = rectangle_area(l,w)
print(r_area)