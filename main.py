#Завдання на використання функцій з бібліотекою math:

#1. Площа кола

# import math
#
#
# def circle_area(radius):
#     area = math.pi * radius ** 2
#     return area
#
#
# r = float(input("Enter radius of circle: "))
#
# result = circle_area(r)
#
# print("Area of a circle:", result)
#

#Завдання на використання функцій з бібліотекою date:

#1. Дні між датами

# from datetime import date
#
# def days_between_dates(date1, date2):
#     year1, month1, day1 = map(int, date1.split("-"))
#     year2, month2, day2 = map(int, date2.split("-"))
#
#     first_date = date(year1, month1, day1)
#     second_date = date(year2, month2, day2)
#
#     difference = abs((second_date - first_date).days)
#
#     return difference
#
#
# date1 = input("Enter first date (YYYY-MM-DD): ")
# date2 = input("Enter second date(YYYY-MM-DD): ")
#
# result = days_between_dates(date1, date2)
#
# print("Number of days between dates:", result)


#Завдання на використання функцій з бібліотекою math:

#2. Обчислення факторіалу

# import math
#
# def factorial_number(n):
#     return math.factorial(n)
#
# number = int(input("Enter a number: "))
#
# result = factorial_number(number)
#
# print("Factorial of a number", number, "equal", result)

# Завдання на використання функцій з бібліотекою date:

# 2. Форматування дати

# from datetime import datetime
#
# def format_date(date):
#     date = datetime.strptime(date, "%Y-%m-%d")
#     return date.strftime("%d/%m/%Y")
#
#
# date = input("Enter the date in the format YYYY-MM-DD: ")
#
# result = format_date(date)
#
# print("Date in the new format:", result)

# Завдання на використання функцій з бібліотекою math (високий рівень):
# 1. Обчислення площі еліпса

import math

#Create a function to calculate the area of an ellipse
def ploshad_ellipsa(a, b):
    # Calculate the area using the formula S = pi * a * b
    s = math.pi * a * b

    # Return the result
    return s


# Enter the major semi-axis
a = float(input("Enter the major semi-axis: "))

# Enter the minor semi-axis
b = float(input("Enter the minor semi-axis: "))

# Call the function and save the result
s = ploshad_ellipsa(a, b)

# Print the area rounded to two decimal places
print("The area of the ellipse is:", round(s, 2))
