#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_items = a_dictionary.items()
    sorted_items = sorted(dict_items)
    for i in sorted_items:
        print(f"{i[0]}: {i[1]}")
