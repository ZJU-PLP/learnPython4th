# -*- coding: utf-8 -*-
# @Time    : 2018/7/3 0003 9:39
# @Author  : Lingpeng Peng
# @FileName: exercise30.py
# @Description: else and if-statements
# @GitHub  ：https://github.com/ZJU-PLP

people = 30
cars = 40
buses = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if buses > cars:
    print("That's too many buses.")
elif buses < cars:
    print("Maybe we could take the buses.")
else:
    print("We still can't decide.")

if people > buses:
    print("All right, let's just take the buses.")
else:
    print("Fine, let's stay at home then.")













