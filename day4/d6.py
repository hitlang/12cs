# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang

test_data = [1, 2, 0, -1]


def test(x, y, z, w):
    return x + y + z + w

def test2(*args): # 参数收集 - 》元组
    print(args)

if __name__ == '__main__':
    # r = test(*test_data) # 序列的解包
    # print(r)
    test2(*test_data) #很容易混淆 1， 列表解包， 2 ，然后被*args 封包成元组
    # test2(1, 2, 43, 4, "abc",1)


