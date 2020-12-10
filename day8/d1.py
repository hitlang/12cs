#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
test_data = [1,2,3,4]

# def foo(x):
#
#     return -x

iter = map(lambda x : -x, test_data) #   可迭代对象

for i in iter:

    print(i)

