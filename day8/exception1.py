#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''

'''



try:
    x, y = int(input("第一个数")), int(input("第二个数"))

    r = open("abc.txt")

    r = x / y # 业务逻辑

    r.close()

    print(r)

except Exception as e:

    print("输入错误")
    pass

finally:
    r.close()




print("程序执行完成")