#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
不定长
'''
def foo(y = 1, x = "abc" ,*args): # args 接收任意多个位置参数
    print(args)
    print(x)
    print(y)
    pass
if __name__ == '__main__':
    foo(1,2,3,4,[1,2])
    pass