# -*- coding: utf-8 -*-
# @Time    : 2018/6/21 0021 10:00
# @Author  : Lingpeng Peng
# @FileName: exercise14.py
# @Description: prompt and transmit
# @GitHub  ：https://github.com/ZJU-PLP

from sys import argv

script, usr_name = argv
prompt = '> '

print("Hi %s, I'm the %s script." % (usr_name, script))
print("I'd like to ask you a few question.")
print("Do you like me %s" % usr_name)
likes = input(prompt)

print("Where do you live %s" % usr_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said %r liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer))






















