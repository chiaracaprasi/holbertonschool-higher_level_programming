#!/usr/bin/python3
""" Module rectangle """
from models.base import Base


class Rectangle(Base):
    """Represents a subclass of Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getter of width."""
        return self.__width

    @property
    def height(self):
        """ Getter of height."""
        return self.__height

    @property
    def x(self):
        """ Getter of x."""
        return self.__x

    @property
    def y(self):
        """ Getter of y."""
        return self.__y

    @width.setter
    def width(self, value):
        """ Setter of width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ Setter of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ Setter of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ Setter of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area value of the Rectangle instance """
        return self.__height * self.__width

    def display(self):
        """Prints in stdout the Rectangle instance with # """
        for k in range(self.y):
            print()
        for i in range(self.height):
            for n in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end='')
            print()

    def __str__(self):
        """Overridding __str__ method """
        w = self.width
        h = self.height
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - {w}/{h}")

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        for arg, attr in enumerate(args):
            if arg == 0:
                self.id = attr
            if arg == 1:
                self.width = attr
            if arg == 2:
                self.height = attr
            if arg == 3:
                self.x = attr
            if arg == 4:
                self.y = attr

        if not args:
            for key, value in kwargs.items():
                if 'id' in kwargs:
                    self.id = kwargs["id"]
                if 'width' in kwargs:
                    self.width = kwargs["width"]
                if 'height' in kwargs:
                    self.height = kwargs["height"]
                if 'x' in kwargs:
                    self.x = kwargs["x"]
                if 'y' in kwargs:
                    self.y = kwargs["y"]

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle """
        d = {}
        d["id"] = self.id
        d["width"] = self.width
        d["height"] = self.height
        d["x"] = self.x
        d["y"] = self.y

        return d
