#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

'''
定义一个函数，迭代输出，列表元素
一个py文件。就是一个模块，模块名，是文件名
'''
def  printList(x):
    '''

    :param x:  是一个列表 ,x是局部变量，
    :return:
    '''
    if isinstance(x,list) or isinstance(x,tuple):
        for i in x:
            print(i)






if __name__ == '__main__':
    test_data = [1, 2, 3, ]  # 全局
    test_data1 = (1, 2, 5,)  # 全局
    printList(test_data1)
    pass

