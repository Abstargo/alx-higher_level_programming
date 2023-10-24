#!/usr/bin/python3

"""Define a square class"""


class Square:
    """
    Represents a square.

    Attributes:
        size (float or int): The size of the square.

    Methods:
        size(self): Retrieve the size of the square.
        size(self, value): Set the size of the square.
        area(self): Calculate the area of the square.
        __eq__(self, other): Compare if two squares have equal areas.
        __ne__(self, other): Compare if two squares have unequal areas.
        __lt__(self, other): Compare if the area of the first square
        is less than the second square.
        __le__(self, other): Compare if the area of the first square
        is less than or equal to the second square.
        __gt__(self, other): Compare if the area of the first square
        is greater than the second square.
        __ge__(self, other): Compare if the area of the first square
        is greater than or equal to the second square.
    """

    def __init__(self, size=0):
        """
        Initialize a Square instance with a specified size.

        Args:
            size (float or int, optional): The size of the square.
            Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (float or int): The size of the square.

        Raises:
            TypeError: If the size is not a number.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compare if two squares have equal areas.

        Args:
            other (Square): Another Square object.

        Returns:
            bool: True if areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compare if two squares have unequal areas.

        Args:
            other (Square): Another Square object.

        Returns:
            bool: True if areas are unequal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Compare if the area of the first square is less than the second square.

        Args:
            other (Square): Another Square object.

        Returns:
            bool: True if area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compare if the area of the first square is less
        than or equal to the second square.

        Args:
            other (Square): Another Square object.

        Returns:
            bool: True if area is less or equal, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Compare if the area of the first square is greater
        than the second square.

        Args:
            other (Square): Another Square object.

        Returns:
            bool: True if area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compare if the area of the first square is greater
        than or equal to the second square.

        Args:
            other (Square): Another Square object.

        Returns:
            bool: True if area is greater or equal, False otherwise.
        """
        return self.area() >= other.area()
