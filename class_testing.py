"""testing change attributes in python class
"""


class Employee:
    """Employee Class
    """

    def __init__(self, name):
        self.name = name
        self.salary_per_hour = 50
        self.hour_per_day = 5

    def calculate_salary(self):
        """calculate employee salary

        Returns:
            int: salary
        """
        return self.salary_per_hour * self.hour_per_day * 20

    def show_info(self):
        """show employee information

        Returns:
            str: full information
        """
        information = (f"Employee Information...\n"
                       f"Class: {self.__class__.__name__}\n"
                       f"Name: {self.name}\n"
                       f"Salary(Month): {self.calculate_salary()}$\n"
                       f"Salary(Hour): {self.salary_per_hour}$\n"
                       f"Work Time: {self.hour_per_day}H")

        return information


class Contractor(Employee):
    """Contractor Class(Employee subclass)
    """

    def __init__(self, name):
        super().__init__(name)
        self.salary_per_hour = 100


class FullTimeEmployee(Employee):
    """Full Time Employee Class(Employee subclass)
    """

    def __init__(self, name):
        super().__init__(name)
        self.hour_per_day = 8


print(Employee('Salar').show_info())

print('---------------------------------')

print(Contractor('Mohammad').show_info())

print('---------------------------------')

print(FullTimeEmployee('Dori').show_info())
