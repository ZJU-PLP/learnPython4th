# -*- coding: utf-8 -*-
# @Time    : 2018/7/5 0005 15:18
# @Author  : Lingpeng Peng
# @FileName: exercise42_prepare.py
# @Description: the introduction of Class
# @GitHub  ：https://github.com/ZJU-PLP
# @Comment : Tab == 4 spaces


class TheThing(object):

    def __init__(self):
        self.number = 0

    def some_function(self):
        print("I got called.")

    def add_me_up(self, more):
        self.number += more
        return self.number


# two different things
a = TheThing()
b = TheThing()

a.some_function()
b.some_function()

print(a.add_me_up(20))
print(a.add_me_up(20))
print(b.add_me_up(30))
print(b.add_me_up(30))  # 为什么打印出来的不是30？

print(a.number)
print(b.number)


















