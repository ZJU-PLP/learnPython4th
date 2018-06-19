# -*- coding: utf-8 -*-
# @Time    : 2018/6/19 0019 19:30
# @Author  : Lingpeng Peng
# @FileName: exercise06.py
# @Description: string
# @GitHub  ：https://github.com/ZJU-PLP

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who known %s and those who %s." % (binary, do_not)

print(x)
print(y)

print("I said : %r." % x)
print("I also said: %s." % y)

hilarious = False

# add the function of comparing %s and %r
test = 'good'
joke_evaluation_r = "Isn't that joke so funny?! %r."
joke_evaluation_s = "Isn't that joke so funny?! %s."

print(joke_evaluation_r % hilarious)
print(joke_evaluation_r % test)
print(joke_evaluation_s % test)
w = "This is the left side of ..."
e = "a string with a right side."

print(w + e)










