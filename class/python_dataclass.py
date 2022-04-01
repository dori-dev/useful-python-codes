"""dataclasses example in python
"""

from dataclasses import dataclass, field


@dataclass(order=True, frozen=True)
class Person:
    """Human(Person)"""
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    strength: int = 100

    def __post_init__(self):
        object.__setattr__(self, 'sort_index', self.strength)

    def add_age(self, value: int):
        """add number to age

        Args:
            value (int): value for add to age
        """
        object.__setattr__(self, 'age', self.age+value)


person1 = Person("Mohammad", "Developer", 17)
person2 = Person("Salar", "Student", 16)
person3 = Person("Dori", "Body Builder", 20)

print(person1.age)
person1.add_age(10)
print(person1.age)

print(person1)

print(person3 == person2)
print(person1 < person2)
