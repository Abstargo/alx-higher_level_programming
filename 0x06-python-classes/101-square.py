#!/usr/bin/python3

"""Define a Square class"""


class Square:
    """
    This class defines a square.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.

    Methods:
        size: Getter method to retrieve the size of the square.
        size.setter: Setter method to set the size of the square.
        position: Getter method to retrieve the position of the square.
        position.setter: Setter method to set the position of the square.
        area: Computes and returns the area of the square.
        my_print: Prints the square with the character '#' to stdout.

    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int, optional): The size of the square (default is 0).
            position (tuple, optional): The position of
            the square (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer, or
            if position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if not isinstance(position, tuple) or len(position) != 2 or
           not all(isinstance(i, int) and i >= 0 for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        Getter method to retrieve the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method to set the position of the square.

        Args:
            value (tuple): The new position value.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or
           not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' to stdout.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A string representation of the square.
        """
        return self.__str__()


if __name__ == "__main__":
    my_square = Square(5, (0, 0))
    my_square.my_print()

    print("--")

    my_square = Square(5, (4, 1))
    my_square.my_print()
