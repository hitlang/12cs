#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

import  requests


res = requests.get(url="http://localhost:9000/users", params={ "abc": "kevin"})



print(res.text)
