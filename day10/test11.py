#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

# 获得数据库连接
import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             port= 3307,
                             password='123456',
                             db='student',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)


print(connection)
