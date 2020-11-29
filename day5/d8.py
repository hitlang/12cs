#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
偏函数
'''
from functools import partial

def add(x = 1 , y = 2, z = None):
    if isinstance(z,  int): #数据类型验证
        return x + y + z

    return x + y

f  = partial(add, x = 1, y = 2) #偏函数

x =  f(z= 1)
print(x)
x =  f(z= 2)
print(x)
x =  f(z= 3)
print(x)
x =  f(z= 4)
print(x)

#
#
# if __name__ == '__main__':
#     r =  add()
#     assert  3 == r, "断言失败"
#
#     r =  add(z = 1)
#     assert  4 == r, "断言失败"
#
#     r = add(z = 2)
#     assert 5 == r, "断言失败"
#     pass
