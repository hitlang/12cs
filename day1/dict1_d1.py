# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
函数，只干一件事情。-》高内聚
为了复用
'''
#字典
def  first_func():
        stu = {
            "studentNo": "001",
            "studentName": "陈超",
            "phone": "1212312",
            "address": "武汉",
            "bornDate": "2020/9/8",
            "gradeId": 3
        }
        #读取字典数据
        # print("获取学生编号", stu["xxxxx"])
        print(stu.get("gradeId"))
        #删除数据
        del stu["gradeId"]
        print(stu)
        # 增加数据
        stu["country"] = "中国"
        print(stu)
        #
        stu['country'] = "新加坡"
        print(stu)

        #update 增加或修改数据
        stu.update({
            "gender" : 1,
            "country":"荷兰"
        })

        print(stu)

        r = stu.popitem() # 删除，并返回字典最下面一项
        #
        print(r)

        print(stu)


