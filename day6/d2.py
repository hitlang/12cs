#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

list1 = [ 3, 2, 1, 4 ,5]

# list1.insert(2, 0)
list1[2:2] = [0] # 等价于 切片赋值

print(list1)

del list1[-1] #

print(list1)

last  = list1.pop()

print(list1)

last2 = list1.pop(-2)

assert  last2 == 0 , "0没有被删除"

print(list1)







