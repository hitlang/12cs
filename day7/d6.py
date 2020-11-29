#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
位置参数
'''
def foo(x , y = 1):

    print(x , y)

if __name__ == '__main__':
    foo(2,4)
    foo(2)
    pass