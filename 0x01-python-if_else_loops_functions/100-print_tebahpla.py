#!/usr/bin/python3

for letter in reversed(range(97, 123)):
    if letter % 2 != 0:
        letter = letter - 32
    print(chr(letter), end="")
