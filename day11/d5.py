#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

class Person:

    def __init__(self, name) -> None:
        self.name = name

    def  say(self):
        print("{} is saying".format(self.name))


class Student(Person):

    def __init__(self, name, age) -> None:
        super().__init__(name) #python3 固定写法
        self.age = age

    def  info(self):
        print("name = {}, age = {}".format(self.name, self.age))
    #方法覆盖
    def say(self):
        print("-----------------------------")


if __name__ == '__main__':
    s1 = Student("kevin", 19)

    s1.say()

    s1.info()
