"""Abstraction in python
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Shape Class
    """

    @abstractmethod
    def area(self):
        """area of shape
        """

    @abstractmethod
    def perimeter(self):
        """perimeter of shape
        """


class Square(Shape):
    """Square Class(Shape subclass)
    """

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 4


class Circle(Shape):
    """Circle Class(Shape Subclass)
    """
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.PI * self.radius ** 2

    def perimeter(self):
        return 2 * self.PI * self.radius


# square object
square = Square(5)
print(square.area())
print(square.perimeter())

# circle object
circle = Circle(2)
print(circle.area())
print(circle.perimeter())
