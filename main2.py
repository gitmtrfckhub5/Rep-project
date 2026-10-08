#Завдання на використання функцій з бібліотекою math:

#2. Обчислення факторіалу

import math

def factorial_number(n):
    return math.factorial(n)

number = int(input("Enter a number: "))

result = factorial_number(number)

print("Factorial of a number", number, "equal", result)