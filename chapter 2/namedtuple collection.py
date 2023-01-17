from collections import namedtuple

City = namedtuple("city", "name country population coordinates")

tokyo = City("Tokyo", "JP", 36.933, (35.689722, 139.691667))

print(tokyo.coordinates)
print(tokyo.name)

print(tokyo[0])
print(tokyo[1])
