#!/usr/bin/python3
""" Module square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a subclass of Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ Getter of size."""
        return self.width

    @size.setter
    def size(self, value):
        """ Setter of size """
        self.width = value
        self.height = value

    def __str__(self):
        """Overridding __str__ method """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")


    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args is not None and len(args) != 0:
            for arg, attr in enumerate(args):
                if arg == 0:
                    self.id = attr
                if arg == 1:
                    self.size = attr
                if arg == 2:
                    self.x = attr
                if arg == 3:
                    self.y = attr

        else:
            for key, value in kwargs.items():
                if 'id' in kwargs:
                    self.id = kwargs["id"]
                if 'size' in kwargs:
                    self.size = kwargs["size"]
                if 'x' in kwargs:
                    self.x = kwargs["x"]
                if 'y' in kwargs:
                    self.y = kwargs["y"]
