#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = list(set(my_list))
    res = sum(unique_numbers)
    return res
