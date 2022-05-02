#!/usr/bin/python3


def no_c(my_string):
    char_to_remove = {67: None, 99: None}
    return(my_string.translate(char_to_remove))
