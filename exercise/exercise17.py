# -*- coding: utf-8 -*-
# @Time    : 2018/6/21 0021 13:32
# @Author  : Lingpeng Peng
# @FileName: exercise17.py
# @Description: more documents operation
# @GitHub  ：https://github.com/ZJU-PLP

from sys import argv
from os.path import exists  # python中的os模块:http://www.cnblogs.com/MnCu8261/p/5483657.html

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

# we would do these two on one line too, how?
input = open(from_file)
indata = input.read()

print("The input file is %d bytes long" % len(indata))

print("Does the file exist? %r" % exists(to_file))
print("Ready, hint RETURN to continue, CTRL-C to abort.")
input()

output = open(to_file, 'w')
output.write(indata)

print("All right, all down.")

output.close()
input.close()






































