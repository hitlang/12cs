#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
import itertools
def generator_data(all):
    '''

    :param all:  是一个列表 ，列表中的元素为列表
    :return:
    '''
    return  [i  for i in itertools.product(*all)]



