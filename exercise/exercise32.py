# -*- coding: utf-8 -*-
# @Time    : 2018/7/3 0003 11:30
# @Author  : Lingpeng Peng
# @FileName: exercise32.py
# @Description: loop and list
# @GitHub  ：https://github.com/ZJU-PLP

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2,  'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print("This is count %d" % number)

# same as above
for fruit in fruits:
    print("A fruit of type %s" % fruit)

# also we can go through mixed lists too
# notice we have to use %r since we don't known what's in it.
for i in change:
    print("I got %r" % i)

# we can also build lists, first start with an empty one
elements = []

# then we use range function to do 0 to 5 counts
for i in range(0, 6):
    print("Adding %d to the list." % i)
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print("Element was: %d" % i)

# add the range function
test = range(0, 6)
for i in test:
    print("Test was： %d" % i)

# list: pop, empty, sort, reverse; insert, update, remove






























