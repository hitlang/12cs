# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
闭包函数
1. 在一个函数内部
2，内部函数，需要访问外部函数的变量
3，外部函数，返回内部函数
'''


g = 1
def ordinary(x):
    global g
    g = 2
    return x + 1

def outer(x=1):
    # 闭包函数
    y = 1
    z = 2
    def inner():

        x = 2
        print(x + y + z)

    return inner


f = outer(g)

print(f.__closure__) #

# print(outer.__closure__)





