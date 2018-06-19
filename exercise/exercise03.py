# -*- coding: utf-8 -*-
# @Time    : 2018/6/19 0019 16:34
# @Author  : Lingpeng Peng
# @FileName: exercise03.py
# @Description: numbers and numbers computing
# @GitHub  ：https://github.com/ZJU-PLP

print("I will now count my chickens:")

print("Hens", 25 + 30 / 6)
print("Roosters", 100 - 25 * 3 % 4)

print("Now, I can count eggs:")

# why the result is 6.75, the result should be 7? python2 and 3 is different, add int!
print(3 + 2 + 1 - 5 + 4 % 2 - int(1 / 4) + 6)

print("Is it true that 3 + 2 < 5 - 7?")

print(3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh , that's why it's false.")

print("How about some more.")

print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)















