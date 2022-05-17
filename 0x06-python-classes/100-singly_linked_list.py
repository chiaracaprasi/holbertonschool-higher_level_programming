#!/usr/bin/python3
"""Represents a node of a singly linked list.
    Private instance attribute: data and next_node
    Instantiation with data and next_node
    Public instance method: sorted
    Singly linked list.
    Private instance attribute: head.
    Simple instantiation.
    Public instance method: def sorted_insert(self, value).
    """


class Node:
    """Represents a class. """
    def __init__(self, data, next_node=None):
        """ Initialise the data."""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ Retrieves the data."""
        return self.__data

    @data.setter
    def data(self, value):
        """ Sets the value of the data."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Retrieves next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Sets the value of the next_node."""
        if value is not None or not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Defines a class"""
    def __init__(self):
        self.__head = None


    def __str__(self):
        """ For printing linked lis"""
        tmp == self.__head
        while tmp:
            print(tmp.data)
            tmp = tmp.next_node
            return str(tmp.data)


    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position
            in the list (increasing order)  """
        
        new_node = Node(value)
        self.__head = new_node
            
