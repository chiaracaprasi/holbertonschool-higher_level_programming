#!/usr/bin/python3
"""
 Module 1-my_list
"""


class MyList(list):
    """a subclass (MyList) of list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """ prints the list in ascending sort"""
        my_sorted_list = []
        for i in sorted(self):
            my_sorted_list.append(i)
        print(my_sorted_list)
