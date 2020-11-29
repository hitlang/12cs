#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
注释 ： 实现了 xx功能
'''
import pprint
x = 1 # 贴着边写的，是模块的全局变量

def  test():

    pass


class Teacher:
    pass
# print(__doc__) # __doc__变量，代表当前模块的文档
#
# print(__name__) # __name__变量 的值是 __main__

pprint.pprint(globals()) #输出当前模块的全局变量
