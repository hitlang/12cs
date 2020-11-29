#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

x = 1

def add():
    x = 2

    def inner():
        nonlocal x
        x +=   2
        print(x)

    return inner

if __name__ == '__main__':
    func = add() #返回一个内部函数对象，并且赋给 func 变量
    func() # 使用变量名 去掉内部inner函数
