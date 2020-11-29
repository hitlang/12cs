#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

class Student:
    #magic
    def __init__(self, name,age) -> None:
        self.name = name
        self.age = age


    def info(self):
        print("学生的姓名:{},学生的年纪{}".format(self.name, self.age))
if __name__ == '__main__':
    s1 = Student("kevin", 19)

    s2 = Student("eric", 19)

    #访问属性

    print(s1.name)

    #调用函数

    s1.info()

    s2.info()






