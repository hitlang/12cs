#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
import time
from selenium import  webdriver


drive = webdriver.Firefox()


time.sleep(5)
page = drive.get("http://127.0.0.1:8000/form1.html")



drive.close()
