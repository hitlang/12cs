#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

'''
 20 ， 30 ， ‘a’ ,  -1 , 2.34
'''

def my_avg(list):
    '''
    对列表，求平均值
    :param list:
    :return:
    '''
    data = []
    for i in list:
        if isinstance(i, int) or isinstance(i,float):
            data.append(i)

    return  sum(data) / len(data)



if __name__ == '__main__':


    test_data = [20 , 30 , "a",  -1 , 2.34 ]

    print(my_avg(test_data))


