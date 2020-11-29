# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
把 2对应的数据该为 "d" , 3 对应的数据改为 "e" ,增加 4  “4” ，5 “5”
'''
s = {
    1: "a",
    2: "b",
    3: "c",

}
#很重要，也很好用
s.update({
    2: "d",
    3: "e",
    4: "4",
    5: "5"
})

print(s)
