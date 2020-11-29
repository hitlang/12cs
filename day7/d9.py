#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

def test(*x,name= "kevin",age = 18):
	print(name)
	print(age)

if __name__ == '__main__':
    # test("eric", 19)
    # test()
    test(age=10, name="eric") # 会这么去用



