#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
生成测试数据，  0-99之间的偶数的   订单编号 是 "SND_order_x"
'''
gen = ( "SND_order_{}".format(test_data) for test_data in range(100) if test_data % 2 == 0)
print(next(gen))
print(next(gen))
print(next(gen))


