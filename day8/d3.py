#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
def auth(fn):
    #闭包函数
    def inner(**kwargs):
        name = kwargs["name"]
        password = kwargs["password"]
        if name == "kevin" and password == "123456":
            fn(name , password)
        else:
            print("权限不正确")
    return  inner


@auth
def do_something1(name, password):
    print("执行业务操作1")

@auth
def do_something2(name, password):
    print("执行业务操作2")


if __name__ == '__main__':
    # do_something1("kevin", "1234567")
    do_something2(name="kevin", password="12456")
    pass
