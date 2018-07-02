# -*- coding: utf-8 -*-
# @Time    : 2018/6/25 0025 9:22
# @Author  : Lingpeng Peng
# @FileName: exercise21.py
# @Description: return
# @GitHub  ：https://github.com/ZJU-PLP


def add(a, b):
    print("adding %d + %d" % (a, b))
    return a + b


def subtract(a, b):
    print("SUBTRACTING %d - %d" % (a, b))
    return a - b


def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b


def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b


print("Let's go do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age:%d, Height:%d, Weight:%d, IQ:%d" % (age, height, weight, iq))

# A puzzle for the extra credit, type it anyway.
print("Here is the puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes :", what, "Can you do it by hand?")
































