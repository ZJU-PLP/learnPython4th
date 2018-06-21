# -*- coding: utf-8 -*-
# @Time    : 2018/6/21 0021 10:36
# @Author  : Lingpeng Peng
# @FileName: exercise15.py
# @Description: read documents
# @GitHub  ：https://github.com/ZJU-PLP

from sys import argv

script, filename = argv

txt = open(filename)

print("Here's your file %r:" % filename)
print(txt.read())
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())



























