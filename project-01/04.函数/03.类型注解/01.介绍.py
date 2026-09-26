#指定变量类型
a:int = 16
names10: list[str] = ["A","B","C"]
names11: list[str | int] = ["A","B",100,"C",300]
names2: set[str] = {"A","45","123"}
names3: dict[str,int] = {"num":0,"price":45,"score":123}
names4: tuple[str,int,int] = ("A",16,65)

#类型推断
#python解释器会推断其数据类型
b = 4
