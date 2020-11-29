#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
from typing import Any


class Category:

    _instance = None

    def __new__(cls, *args,**kwargs) -> Any:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            return cls._instance
        else:
            return cls._instance

    def __init__(self, class_id, class_name) -> None:
        self.class_id = class_id
        self.class_name = class_name
        self.sub_list = []

    def  add_category(self,category):
        '''
        增加子类别
        :param category:
        :return:
        '''
        self.sub_list.append(category)

    def __iter__(self):
        '''
        如果类中有这个方法，那么这个对象是可迭代对象

        :return:
        '''
        return iter(self.sub_list)

    # def  info(self):
    #     '''
    #     打印子类别
    #     :return:
    #     '''
    #     for i in self.sub_list:
    #         print(i)

    def __str__(self) -> str:
        return "Category id == {} , name = {}".format(self.class_id,self.class_name)



if __name__ == '__main__':
    s1 = Category("1", "abc")
    s2 = Category("1", "abc")
    s3 = Category("1", "abcd")

    print(id(s1),id(s2), id(s3))
    # c1.add_category(s1)
    # c1.add_category(s2)
    #
    # #查看家用电器的子类别
    #
    # # c1.info()
    #
    #
    # for i in c1:
    #     print(i)

    pass






