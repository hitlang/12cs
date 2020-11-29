# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
字典的比较和过滤 条件 ：
'''
dict1 = {
    "studentNo": "001",
    "studentName": "陈超",
    "phone": "1212312",
    "address": "武汉",
    "bornDate": "2020/9/8",
    "gradeId": 3
}



dict2 = {  k:v  for k , v in dict1.items() if k.startswith("s")}

print(dict2)




