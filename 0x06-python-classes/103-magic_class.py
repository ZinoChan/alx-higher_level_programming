#!/usr/bin/python3
import math


class MagicClass:
    def __init__(self, radius=0):
        """
        Initializes a MagicClass object with a given radius.

        Args:
            radius (int or float, optional): The radius of the MagicClass object. Defaults to 0.

        Raises:
            TypeError: If the radius provided is not a number (int or float).
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the MagicClass object.

        Returns:
            float: The area of the MagicClass object.

        Formula:
            area = pi * radius^2
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the MagicClass object.

        Returns:
            float: The circumference of the MagicClass object.

        Formula:
            circumference = 2 * pi * radius
        """
        return 2 * math.pi * self.__radius
