#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

'''
逐行读取
'''

# f = open("test_data.txt", encoding="utf8")
#
# for line in f:
#
#     print(line)
#
# f.close()

#上下文管理器
import pytest

def  gen_test_data():

        with open(r"G:\虫师\python\12_terms\12cs\day7\test_data.txt", encoding="utf8") as f:
                r = f.readlines()

        return r




