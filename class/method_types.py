"""methods type in python classes
- instance method
- class method
- static method
"""
from typing import List
from datetime import datetime

CURRENT_YEAR = datetime.today().year


class Person:
    """
    A class used to represent a Person!

    Attributes
    ----------
    name: str
        person name
    age: int
        person age

    Methods
    -------
    add_task(name, time, priority)
        add task to tasks list
    show_tasks(sort_by="priority")
        show sorted tasks
    get_population()
        show people populations
    from_birthdate(name, birthyear)
        create `Person` object with birthday
    is_adult(age)
        is person adult or not
    """
    population = 0

    def __init__(self, name: str, age: int):
        self.name = name.title()
        self.age = abs(age)
        self.tasks: List[tuple] = []
        Person.population += 1
        self.adult = self.is_adult(self.age)

    def add_task(self, name: str, time: str, priority: str):
        """add task to tasks list

        Args:
            name (str): task name
            time (str): task time
            priority (str): task priority
        """
        self.tasks.append((name, time, priority))

    def show_tasks(self, sort_by: str = "priority") -> None:
        """show all tasks

        Args:
            sort_by (str, optional): sort task by. Defaults to "priority".
        """
        print("TASKS:")
        tasks: List[tuple] = self._sorted_tasks(sort_by)
        for name, time, priority in tasks:
            print(f'"{name}" in {time}\' with '
                  f'priority({priority})')

    def _sorted_tasks(self, sort_by: str) -> List[tuple]:
        """sorted tasks with `sort_by`

        Args:
            sort_by (str): [-][time|priority|name]

        Returns:
            List[tuple]: list of sorted task
        """
        reversed_ = False
        if sort_by[0] == "-":
            sort_by = sort_by[1:]
            reversed_ = True
        if sort_by.lower() == "priority":
            tasks = sorted(
                self.tasks, key=lambda task: task[2],
                reverse=reversed_)
        elif sort_by.lower() == "time":
            tasks = sorted(
                self.tasks, key=lambda task: task[1],
                reverse=reversed_)
        elif sort_by.lower() == "name":
            tasks = sorted(
                self.tasks, key=lambda task: task[0],
                reverse=reversed_)
        else:
            tasks = self.tasks
        return tasks

    @classmethod
    def get_population(cls) -> int:
        """get population of people

        Returns:
            int: pepole populations
        """
        return cls.population

    @classmethod
    def from_birthdate(cls, name: str, birthyear: int) -> object:
        """create Person object with birthday

        Args:
            name (str): person name
            birthyear (int): person birthyear

        Returns:
            Person: person object
        """
        age: int = CURRENT_YEAR - birthyear
        return Person(name, age)

    @staticmethod
    def is_adult(age: int) -> bool:
        """is person adult

        Args:
            age (int): person age

        Returns:
            bool: adult(True) | not adult(False)
        """
        if age >= 18:
            return True
        return False

    def __repr__(self) -> str:
        class_ = self.__class__.__name__
        return f"{class_}({repr(self.name)}, {self.age})"


if __name__ == "__main__":
    p1 = Person('ali', 20)
    print(p1.adult)
    p1.add_task("washing car", 20, 3)
    p1.add_task("cleaning room", 45, 2)
    p1.add_task('homework', 40, 1)
    p1.show_tasks("priority")
    p2 = Person('mohammad', 16)
    print(p2.adult)
    print(Person.get_population())
    p3 = Person.from_birthdate('zahra', 2004)
    print(p3)
    print(p3.age)
