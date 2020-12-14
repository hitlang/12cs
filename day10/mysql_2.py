# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang

import pymysql.cursors

# Connect to the database

# 获得数据库连接
connection = pymysql.connect(host='localhost',
                             user='root',
                             port=3307,
                             password='123456',
                             db='student',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
try:

    with connection.cursor() as cursor:

        # sql = 'select studentNo ,studentName from student where gradeId = %s'

        sql = "INSERT INTO `subject` (`subject_no`, `subject_name`, `ks`, `term_no`) VALUES (%s, %s, %s, %s)"

        cursor.execute(sql, (4, 'oop', 100, 1))

        connection.commit()





finally:
    connection.close()
