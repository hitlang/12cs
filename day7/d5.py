#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
可变对象，调用函数的时候，传地址，不可变，传值
'''

def change_list(list1):
    list1.append("1")

test_data = [1,2,3]

change_list(test_data)

print(test_data)

