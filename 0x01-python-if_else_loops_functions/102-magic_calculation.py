#!/usr/bin/python3


def uppercase(str):
    for char in str:
        char_value = ord(char)
        if char_value >= 97 and char_value <= 122:
            char = chr(char_value - 32)
        print(char, end="")
    print()
