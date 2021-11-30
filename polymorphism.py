"""Polymorphism example
"""


class Person:
    """Person Class
    """

    def __init__(self, name: str, family: str, age: int):
        self.name = name
        self.family = family
        self.age = age

    def __str__(self):
        return f"{self.name} {self.family}, {self.age} year"

    def add_age(self):
        """add one year to age
        """
        self.age += 1

    def change_info(self, **variables):
        """change person information

        Args:
            name (str): person name
            family (str): person family
            age (int): person age
        """

        self.name = variables.get("name", self.name)
        self.family = variables.get("family", self.family)
        self.age = variables.get("age", self.age)


class Employee(Person):
    """Employee Class
    """

    def __init__(self, name: str, family: str, age: int, salary: int):
        super().__init__(name, family, age)
        self.salary = salary

    def __str__(self):
        return f"{super().__str__()}, {self.salary}$"

    def add_salary(self, value: int):
        """add value to salary
        """
        self.salary += value

    def change_info(self, **variables):
        """change employee information

        Args:
            name (str): employee name
            family (str): employee family
            age (int): employee age
            salary (int): employee salary
        """

        super().change_info(**variables)
        self.salary = variables.get("salary", self.salary)
