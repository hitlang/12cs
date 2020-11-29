#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
循环结构 ,一定要能跳出来
'''
# count = 0
# while True:
#     print("abc")
#     count += 1
#     if count == 100:
#         break #跳出循环

count = 0
while count < 20:
    count += 1
    if count == 10:
        continue  # 进入下一个迭代
    print( str(count) + "abc")



