#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
排序
'''
        # -3 -2 -1 -4 -5  -> 5 , 4  3  2 1
list1 = [ 3, 2, 1, 4 ,5]

# list1.sort()
#
# print(list1)
# def fun(y):
#
#     return -y

list2 = sorted(list1, key=lambda  x : -x) # 返回一个新的升序排序后的列表
#
# print(id(list2))
# print(id(list1))

#排序规则

print(list2)




