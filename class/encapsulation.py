"""python encapsulation example
"""


class Person:
    """person class

    Args:
        name (str): name of person
        age (age): age of person
    """

    def __init__(self, name: str, age: int):
        self.__name = name.title()
        self.__age = abs(age)

    @property
    def name(self) -> str:
        """name getter

        Returns:
            str: person name
        """
        return self.__name

    @name.setter
    def name(self, new_name: str):
        """name setter

        Args:
            new_name (str): new person name
        """
        self.__name = new_name.title()

    @name.deleter
    def name(self):
        self.__name = ""

    @property
    def age(self) -> int:
        """age getter

        Returns:
            int: person age
        """
        return self.__age

    @age.setter
    def age(self, new_age: int):
        """age setter

        Args:
            new_age (int): new person age
        """
        self.__age = abs(new_age)

    @age.deleter
    def age(self):
        self.__age = 0

    def __repr__(self):
        class_ = self.__class__.__name__
        return f"{class_}({repr(self.__name)}, {self.__age})"


if __name__ == "__main__":
    # create objects
    person1 = Person("ali", 20)
    person2 = Person("mohammad", 16)
    # print objects
    print(person1)
    print(person2)
    # set attributes
    person1.name = "alireza"
    print(person1)
    person2.age = 17
    print(person2)
    # get attributes
    print(person1.age)
    print(person2.name)
    # delete attributes
    del person1.age
    print(person1)
    del person2.name
    print(person2)
