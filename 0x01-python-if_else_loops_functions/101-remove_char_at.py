#!/usr/bin/python3


def remove_char_at(str, n):

    new_str = str
    new_str = new_str[:n] + new_str[n+1:]
    return new_str
