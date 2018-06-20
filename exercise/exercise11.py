# -*- coding: utf-8 -*-
# @Time    : 2018/6/20 0020 13:37
# @Author  : Lingpeng Peng
# @FileName: exercise11.py
# @Description: Ask a question
# @GitHub  ：https://github.com/ZJU-PLP

# 在python3.x中raw_input( )和input( )进行了整合，去除了raw_input( )，仅保留了input( )函数，其接收任意任性输入，将所有输入默认为字符串处理，并返回字符串类型。
print("How old are you?",)
age = input()
print("How tall are you?",)
height = input()
print("How much do you weight?",)
weight = input()

print("So you are %r old, %r tall and %r heavy." % (age, height, weight))















