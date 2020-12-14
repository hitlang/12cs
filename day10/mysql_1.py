#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

import pymysql.cursors

# Connect to the database

# 获得数据库连接
connection = pymysql.connect(host='localhost',
                             user='root',
                             port= 3307,
                             password='123456',
                             db='student',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
try:

    with connection.cursor() as cursor:

        sql = 'select studentNo ,studentName from student where gradeId = %s'

        cursor.execute(sql, (1,))

        result = cursor.fetchall()

        print(result)



finally:
    connection.close()