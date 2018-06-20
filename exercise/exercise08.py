# -*- coding: utf-8 -*-
# @Time    : 2018/6/20 0020 10:16
# @Author  : Lingpeng Peng
# @FileName: exercise08.py
# @Description: printings & printings
# @GitHub  ：https://github.com/ZJU-PLP

formatter = "%r %r %r %r"

print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))  # should be "one", "two", "three", "four"instead of "one, two, three, four"
print(formatter % (True, False, False, True))  # remember the True and False should be capital.
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
  "I had this thing.",
  "That you could type up right.",
  "But it didn't sing.",
  "So I said goodnight."
)
      )

