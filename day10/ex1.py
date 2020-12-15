#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
import json

from student import Student

'''
1. 从数据库中，导出student 表数据为json , 使用json模块，读文件 ，
把所有学生数据，转换为 对象，并 迭代输出， “学生名：xx，  学生编号”

'''
#返回一个文件对象
f = open("student.json" , encoding="utf8")

r = json.load(f) # 返回一个python对象

print(r)

test_data = r['RECORDS']

for s in test_data:

    x = Student( name = s['studentName'], age = None, xh = s['studentNo'])
    print(x)
    pass

