# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
函数，如果有明确的返回值。return  + 表达式
'''


# def foo():
#
#     print("foo")
#     return 1
#
# x = foo()
#
# print(x)

def foo():
    '''

    :return: 函数可以返回多个值
    '''
    return 1, 2, 3, 4, 5


x = foo()
_, *remain = x

print(_)