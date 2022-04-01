"""name tuples"""

from collections import namedtuple


Person = namedtuple("person", "name age height")

p1 = Person('mohammad', 16, 180)
print(p1)
print(p1[1])
print(p1.name)
print(getattr(p1, 'height'))

print(p1._asdict())
print(p1._fields)
p1 = p1._replace(name='dori')
print(p1)

info = ['bob', 20, 175]
p2 = Person._make(info)
print(p2)
print(p2.name)

data = {
    'name': 'john',
    'age': 40,
    'height': 160,
}

p3 = Person(**data)
print(p3)
print(p3)
