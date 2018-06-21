# -*- coding: utf-8 -*-
# @Time    : 2018/6/21 0021 11:11
# @Author  : Lingpeng Peng
# @FileName: exercise16.py
# @Description: read and write documents
# @GitHub  ：https://github.com/ZJU-PLP

"""
function:
close – 关闭文件。跟你编辑器的 文件->保存.. 一个意思。 .
read – 读取文件内容。你可以把结果赋给一个变量。
readline – 读取文本文件中的一行。
truncate – 清空文件，请小心使用该命令。
write(stuff) – 将stuff写入文件。
"""
from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C(^C).")
print("If you don want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")

target.truncate()

print("Now I ask you for three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()






































