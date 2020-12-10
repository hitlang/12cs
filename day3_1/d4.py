#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
局部变量 : 写在函数中的
'''

def foo2():

    print("foo2 中x 的值 为",x)

x = 3



def  foo():

    # global x #  声明 x是全局变量
    x  = 1 #定义了一个 叫 x的局部变量

    print("x的值 ==" ,x)



#for simple test:
if __name__ == '__main__':

    foo()
    foo2()
