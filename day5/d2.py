#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
部分解包 -- 》序列 （字符串，列表，元组）
'''
_ , *middle , _ = [1, 2, 3, 4, 100] # middle是列表

avg = sum(middle) / len(middle)

print(avg)

