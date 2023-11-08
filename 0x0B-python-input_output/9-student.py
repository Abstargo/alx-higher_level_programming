#!/usr/bin/python3

"""Define a class"""


class Student:
    """Defines a student with first_name, last_name, and age"""
    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance with provided fist_...
           Args:
            frist_name (str): The first name of student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        return self.__dict__
