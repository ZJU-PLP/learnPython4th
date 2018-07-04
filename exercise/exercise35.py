
# -*- coding: utf-8 -*-
# @Time    : 2018/7/4 0004 9:48
# @Author  : Lingpeng Peng
# @FileName: exercise35.py
# @Description: branch and function & line 17-18's question
# @GitHub  ：https://github.com/ZJU-PLP

from sys import exit


def gold_room():
    print("The room is full of gold. How much do you take?")

    next = input("> ")
    if "0" in next or "1" in next:
        # how to fix the bug?
        # if "one" in next or "two" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard")  # dead() is defined below


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        next = input("> ")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            print("The bear gets pissed off and chews your leg off.")
        elif next == "open_door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee your life and eating your head?")

    next = input("> ")
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well, that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)


def start():
    print("You are in a dark room.")
    print("There is a door to your right and door.")
    print("Which one do you take?")

    next = input("> ")
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        print("You stumble around the room until you starve.")


start()











































