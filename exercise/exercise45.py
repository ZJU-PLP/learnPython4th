# -*- coding: utf-8 -*-
# @Time    : 2018/7/6 0006 16:04
# @Author  : Lingpeng Peng
# @FileName: exercise45.py
# @Description: object, class and attributes
# @GitHub  ：https://github.com/ZJU-PLP
# @Comment : Tab == 4 spaces


# Animal is-a object(yes, some sort of confusing) Look at extra credit
class Animal(object):
    pass


# ?? is-a
class Dog(Animal):

    def __init__(self, name):
        # ? has-a
        self.name = name


# ?? is-a
class Cat(Animal):

    def __init__(self, name):
        # ?? has-a
        self.name = name


# ?? is-a
class Person(object):

    def __init__(self, name):
        # ?? has-a
        self.name = name

        # Person has-a pet of some kind
        self.pet = None


# ?? is-a
class Employee(Person):

    def __init__(self, name, salary):
        # hmm, what's this strange magic
        super(Employee, self).__init__(name)
        # ?? has-a
        self.salary = salary


# ?? is-a
class Fish(object):
    pass


# ?? ia-a
class Salmon(Fish):
    pass


class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog("Rover")

# ?? is-a
satan = Cat("Santan")

# ?? is-a
mary = Person("Mary")

# ?? is-a
mary.pet = satan

# ?? ia-a
frank = Employee("Frank", 120000)

# ?? is-a
frank.pet = rover

# ?? is-a
flipper = Fish()

# ?? ia-a
crouse = Salmon()

# ?? ia-a
harry = Halibut()
