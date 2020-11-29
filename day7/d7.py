# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang

def foo(x, y=1):
    print(x, y)


if __name__ == '__main__':
    foo(y=4, x=1)  # 在调用的时候， x,y就是关键字参数
    foo(x=1)  # 在调用的时候， x,y就是关键字参数
    pass
