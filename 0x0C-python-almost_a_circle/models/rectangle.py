#!/usr/bin/python3
"""rectangle class"""
from models.base import Base


class Rectangle(Base):
    """class rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        Args:
            width: The width of Rectangle.
            height: The height of Rectangle.
            x: The x coordinate of  Rectangle.
            y: The y coordinate of Rectangle.
            id: The identity of Rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
