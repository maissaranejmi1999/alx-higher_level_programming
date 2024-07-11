#!/usr/bin/python3
"""
this module defines a class square
"""


class Square:
    """
    this is a class that defines a square
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value1):
        if not isinstance(value1, int):
            raise TypeError("size must be an integer")
        if value1 < 0:
            raise ValueError("size must be >= 0")
        self.__size = value1

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(v, int) for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(v >= 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

        def area(self):
            return self.__size ** 2

        def my_print(self):
            if self.__size == 0:
                print()
                return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
