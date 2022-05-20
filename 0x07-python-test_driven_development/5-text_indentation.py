#!/usr/bin/python3
"""

Module text_indentation
Prints a square with the character #

"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of characters: ., ? and :
    Text must be a string otherwise error will occur
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special = ['.', '?', ':']
    flag = 0

    for ch in text:
        if flag == 0:
            if ch == ' ':
                continue
            else:
                flag = -1
        if flag == -1:
            if ch in special:
                print(ch)
                print()
                flag = 0
            else:
                print(ch, end="")
