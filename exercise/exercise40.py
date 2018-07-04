
# -*- coding: utf-8 -*-
# @Time    : 2018/7/4 0004 15:51
# @Author  : Lingpeng Peng
# @FileName: exercise40.py
# @Description: dictionary or dict
# @GitHub  ：https://github.com/ZJU-PLP
# @Comment : Tab == 4 spaces

cities = {'CA': 'San Fransisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'


def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return "Not found."


# add for-loop
for key in cities:
    print(key, cities[key])
    print(cities.items())
    # print(cities[key].items())

# ok pay attention!
cities['_find'] = find_city

while True:
    print("State?(Enter to quit)",)
    state = input("> ")

    if not state: break

    # this line is most important ever! study!
    city_found = cities['_find'](cities, state)
    print(city_found)
    # print(cities[1])













