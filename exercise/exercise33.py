# -*- coding: utf-8 -*-
# @Time    : 2018/7/3 0003 13:42
# @Author  : Lingpeng Peng
# @FileName: exercise33.py
# @Description: while-loop and main()
# @GitHub  ：https://github.com/ZJU-PLP

# i = 0
# numbers = []
#
# while i < 6:
#     print("At the top i is %d" % i)
#     numbers.append(i)
#     # i += 1
#     i = i + 1
#     print("Numbers now:", numbers)
#     print("At the bottom i is %d" % i)
#
#
# print("The numbers: ")
#
# for num in numbers:
#     print(num)

# the add quiz


def while_loop(times):
    i = 0
    numbers = []

    while i < times:
        print("At the top i is %d" % i)
        numbers.append(i)
        i += 1
        print("Numbers now:", numbers)
        print("At the bottom i is %d" % i)

    print("The numbers:")
    for num in numbers:
        print(num)


def main():
    init = 2
    while_loop(init)


if __name__ == '__main__':
    main()



















