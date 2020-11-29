# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang

s = {
        1: "a",
        2: "b",
        3: "c",
        4: [ 1 , 2, 3],
        5: { 1, 2, 3}
}


# for key, value in  s.items():
#     print("key = {}, value = {}".format(key, value)) # 字符串的格式化

s.setdefault(4, "d").append(4)
s.setdefault(4, "d").append(5)
s.setdefault(4, "d").append(6)
s.setdefault(4, "d").append(7)

s.setdefault(5,"d").add(4)
s.setdefault(5,"d").add(5)
s.setdefault(5,"d").add(5)

s.setdefault(6,[]).append("a")



print(s)





