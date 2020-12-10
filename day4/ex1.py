#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
import time
'''
统计： 函数的调用执行时间
'''



def foo1(name, password):
    # if name == "kevin" and password == "123456":
        ''''
        业务操作1
        '''
        time.sleep(1)
        print("---执行业务操作1----------------")
        pass


def foo2(name, password):
    # if name == "kevin" and password == "123456":
        ''''
        业务操作1
        '''
        time.sleep(3)
        print("---执行业务操作2----------------")
        pass

if __name__ == '__main__':

    start = time.time()

    foo2("ddd","111")

    end = time.time()

    print(end - start)

    pass