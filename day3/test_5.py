#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
不定长参数， 接收n个位置参数
'''

def test_1(*abc ,x , y = 4):

    print(abc) #为元组


if __name__ == '__main__':
    test_1(1,2,3,3,"dddd", x  = 1)
    pass
