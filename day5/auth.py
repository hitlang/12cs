#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

def auth(fn):
    def inner(self, **kwargs):
        if self.name == "admin":
            fn(self, **kwargs)
        else:
            pass

    return inner
