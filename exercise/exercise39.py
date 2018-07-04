# -*- coding: utf-8 -*-
# @Time    : 2018/7/4 0004 14:48
# @Author  : Lingpeng Peng
# @FileName: exercise39.py
# @Description: the operation of list
# @GitHub  ：https://github.com/ZJU-PLP
# @Comment : Tab == 4 spaces

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("wait there's not 10 things in that list, let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Days", "Nights", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()  # pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
    print("Adding:", next_one)
    stuff.append(next_one)  # append() 方法用于在列表末尾添加新的对象。
    print("There's %d items now." % len(stuff))

print("There we go:", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])  # whoa! fancy
print(stuff.pop())
print(' '.join(stuff))  # what? cool! # Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
print('#'.join(stuff[3:5]))  # super stellar!




























