#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''

'''
class Student:

    school = "武汉大学" #类变量


    def __init__(self, name) -> None:
        self.name = name

    # # @classmethod
    # def print_school(cls):
    #     print(cls.__name__)
    #     pass

    @staticmethod   #普通的函数
    def print_school(self, x , y ):
        print(self, x, y)


if __name__ == '__main__':
    s1 = Student("kevin")
    s2 = Student("kevin")

    # print(s1.school, Student.school) # 类变量数据 ， 被多个实例共享

    # Student.print_school()
    Student.print_school(1,2,3)
    pass