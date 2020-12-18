# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import pymysql
from pymysql import *

# dict函数能创建一个字典对象
mysql_conf = dict(host='localhost',
                  user='root',
                  port=3307,
                  password='123456',
                  db='student',
                  charset='utf8',
                  cursorclass=pymysql.cursors.DictCursor)


class MysqlHelp:
    """mysql常用方法的封装"""

    conn = pymysql.connect(**mysql_conf)  # 获取连接对象
    cr_obj = conn.cursor()  # 获取cursor对象

    @classmethod
    def get(cls, field, table_name, num):
        cls.cr_obj.execute("select %s from %s" % (field, table_name))
        if num == 1:
            return cls.cr_obj.fetchone()  # 获取一数据
        else:
            return cls.cr_obj.fetchall()  # 获取所有的数据

    @classmethod
    def insert(cls, table_name, field_name, field_value):
        st = ""
        for i in field_name:
            if i == field_name[-1]:
                st += "".join(i + ")")
            elif i == field_name[0]:
                st += "".join("(" + i + ",")
            else:
                st += "".join(i + ",")
        field_name = st

        sql = "insert into {}{} values{}".format(table_name, field_name, field_value)
        print(sql)
        ret = cls.cr_obj.execute(sql)

        # cls.cr_obj.execute()

        cls.conn.commit()
        print(ret)

    @classmethod
    def update(cls, table_name, field):
        field_name = field["field_name"]
        field_value = field["field_value"]
        c_field = field["c_field"]
        v_field = field["f_field"]

        field_value = "'" + field_value + "'"
        ret = cls.cr_obj.execute(
            "update {} set {}={} where {}={}".format(table_name, field_name, field_value, c_field, v_field))
        print(ret)

    @classmethod
    def delete(cls, table_name, field_name, field_value):
        field_value = "'" + field_value + "'"
        ret = cls.cr_obj.execute("delete from %s where %s = %s" % (table_name, field_name, field_value))
        print(ret)

    @classmethod
    def close(cls):
        cls.conn.commit()
        cls.cr_obj.close()
        cls.conn.close()


if __name__ == '__main__':
    # # ret = MysqlHelp.get("*", "students", 4)
    # # print(ret)
    # # ret1 = MysqlHelp.insert("students",("name","age","high"),("老王","10","190"))
    # #
    # # ret1 = MysqlHelp.update("students",{"field_name":"high","field_value":"178","c_field":"id","f_field":15})
    # # print(ret1)
    # ret2 = MysqlHelp.delete("students", "name", "老王")
    #
    tableName = "student"

    field_name = ("studentNo", "studentName")

    values = (1212,"kevin1212")

    MysqlHelp.insert(table_name = tableName, field_name= field_name, field_value = values)

    MysqlHelp.close()
