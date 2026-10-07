#Завдання на використання функцій з бібліотекою math:

#1. Площа кола

import math


def circle_area(radius):
    area = math.pi * radius ** 2
    return area


r = float(input("Enter radius of circle: "))

result = circle_area(r)

print("Area of a circle:", result)

