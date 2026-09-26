#教务管理系统
print("""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 1.添加学生信息  2.修改学生信息  3.删除学生信息  4.查询学生信息  5.列出所有学生  6.统计班级成绩  7.退出系统 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # """)
dict = {}
while True:
    num = int(input("请选择操作(1-7):"))
    match num:
        case 1:
            name = input("请输入学生姓名:")
            if name not in dict:
                chinese = int(input("请输入语文成绩:"))
                math = int(input("请输入数学成绩:"))
                english = int(input("请输入英语成绩:"))
                dict[name] = chinese,math,english
            else:
                print("学生信息已存在")
        case 2:
            name = input("请输入要修改成绩的学生的姓名:")
            if name in dict:
                chinese = int(input("请输入语文成绩:"))
                math = int(input("请输入数学成绩:"))
                english = int(input("请输入英语成绩:"))
                dict[name] = chinese, math, english
            else:
                print("学生信息不存在")
        case 3:
            name = input("请输入要删除学生的姓名:")
            if name in dict:
                del dict[name]
                print("删除成功")
            else:
                print("学生信息不存在")
        case 4:
            name = input("请输入要查询学生的姓名:")
            if name in dict:
                chinese,math,english = dict[name]
                print(f"{name},语文成绩:{chinese},数学成绩:{math},英语成绩:{english}")
            else:
                print("学生信息不存在")
        case 5:
            for name, (chinese, math, english) in dict.items():
                print(f"{name},语文成绩:{chinese},数学成绩:{math},英语成绩:{english}")
        case 6:
            if not dict:
                print("暂无学生信息")
            else:
                subject_scores = {
                    "语文": [],
                    "数学": [],
                    "英语": []
                }

                for name, (chinese, math, english) in dict.items():
                    subject_scores["语文"].append((chinese, name))
                    subject_scores["数学"].append((math, name))
                    subject_scores["英语"].append((english, name))

                for subject, records in subject_scores.items():
                    high_score, high_name = max(records, key=lambda item: item[0])
                    low_score, low_name = min(records, key=lambda item: item[0])
                    average = sum(score for score, _ in records) / len(records)

                    print(
                        f"{subject}：最高分 {high_score}（{high_name}），"
                        f"最低分 {low_score}（{low_name}），平均分 {average:.2f}"
                    )
        case 7:
            print("已退出系统")
            break