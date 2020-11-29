#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
不可变的类型。在内存中，只有一个
'''
# x = "abc"
#
# y = "abc"
#
#
# z = "abc"
#
# print(id(x), id(y), id(z))

# x = []
# x1 = []
# x2 = []
# x3 = []
# x4 = []
#
# print(id(x) , id(x4))
#
# print(x == x4)

t1= (1,)
t2= (1,)
t3= (2,)

print(id(t1) == id(t2))
print(id(t2) != id(t3))