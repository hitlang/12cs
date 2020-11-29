# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import json
class Teacher(object):
    def __init__(self, name) -> None:
        self.__firstName, self.__lastName = name

    @property
    def get_full_name(self):
        return "{" + self.__firstName + self.__lastName + "}"

    @get_full_name.setter
    def get_full_name(self, value):
        '''
        :param value: 新名字
        :return:
        '''
        self.__firstName, self.__lastName = value


if __name__ == '__main__':
    # # 读取文件数据
    # with  open("test_data.json" , "rt" , encoding="utf-8") as fp:
    #    test_data =  json.load(fp)
    # saved = [] # 老师的对象列表
    # #创建对象
    # for item in test_data:
    #     saved.append(Teacher(name=item["name"]))
    #
    # #调用方法获取老师的名字
    # for t in saved:
    #     print(t.get_full_name(), file=open("out.txt","at"))
    t = Teacher("张三")
    # print(t.get_full_name)
    t.get_full_name = "小新"
    print(t.get_full_name)
