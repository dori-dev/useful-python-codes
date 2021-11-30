"""Polymorphism example
"""


class Person:
    """Person Object
    """

    def __init__(self, name: str, family: str, age: int):
        self.name = name
        self.family = family
        self.age = age

    def __str__(self):
        return f"{self.name} {self.family}, {self.age}y"

    def add_age(self):
        """add one year to age
        """

        self.age += 1

    def change_info(self, name: str, family: str, age: int):
        """change person information

        Args:
            name (str): person name
            family (str): person family
            age (int): person age
        """

        self.name = name
        self.family = family
        self.age = age
