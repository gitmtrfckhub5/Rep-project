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

# import math
#
# #Create a function to calculate the area of an ellipse
# def ploshad_ellipsa(a, b):
#     # Calculate the area using the formula S = pi * a * b
#     s = math.pi * a * b
#
#     # Return the result
#     return s
#
#
# # Enter the major semi-axis
# a = float(input("Enter the major semi-axis: "))
#
# # Enter the minor semi-axis
# b = float(input("Enter the minor semi-axis: "))
#
# # Call the function and save the result
# s = ploshad_ellipsa(a, b)
#
# # Print the area rounded to two decimal places
# print("The area of the ellipse is:", round(s, 2))


#Завдання на використання функцій з бібліотекою math (високий рівень):
#1. Обчислення площі еліпса

# import math
#
# # Create a function to calculate the area of an ellipse
# def ploshad_ellipsa(a, b):
#     # Calculate the area using the formula S = pi * a * b
#     s = math.pi * a * b
#
#     # Return the result
#     return s
#
#
# # Enter the major semi-axis
# a = float(input("Enter the major semi-axis: "))
#
# # Enter the minor semi-axis
# b = float(input("Enter the minor semi-axis: "))
#
# # Call the function and save the result
# s = ploshad_ellipsa(a, b)
#
# # Print the area rounded to two decimal places
# print("The area of the ellipse is:", round(s, 2))




# #Завдання на використання функцій з бібліотекою date (високий рівень):
# #1. Обчислення часу в дорозі
#
# """Import the datetime library"""
# from datetime import datetime, timedelta
#
# """Create a function to calculate the arrival time"""
# def calculate_arrival(start_time, duration):
#     """Add the trip duration to the start time"""
#     arrival_time = start_time + timedelta(hours=duration)
#
#     """Return the arrival date and time"""
#     return arrival_time
#
#
# """Enter the departure date and time"""
# date_text = input("Enter departure date and time (YYYY-MM-DD HH:MM): ")
#
# """Convert the text to a datetime object"""
# start_time = datetime.strptime(date_text, "%Y-%m-%d %H:%M")
#
# """Enter the trip duration in hours"""
# duration = float(input("Enter trip duration in hours: "))
#
# """Call the function"""
# arrival_time = calculate_arrival(start_time, duration)
#
# """Print the arrival date and time"""
# print("Arrival date and time:", arrival_time.strftime("%Y-%m-%d %H:%M"))



# #Завдання на використання функцій з бібліотекою math
# #2. Гармонічний ряд
#
# """Import the math library"""
# import math
#
# """Create a function to calculate the harmonic series"""
# def harmonic_sum(n):
#     """Set the sum to zero"""
#     total = 0
#
#     """Calculate the sum of the first n terms"""
#     for i in range(1, n + 1):
#         total = total + 1 / i
#
#     """Return the result"""
#     return total
#
#
# """Enter the number of terms"""
# n = int(input("Enter the number of terms: "))
#
# """Call the function"""
# result = harmonic_sum(n)
#
# """Print the result"""
# print("The sum of the harmonic series is:", round(result, 4))


# Завдання на використання функцій з бібліотекою date (високий рівень):

# 2. Генерація календаря для місяця

"""Import the calendar library"""
import calendar

"""Create a function to generate a calendar"""
def generate_calendar(year, month):
    """Create the calendar for the given month and year"""
    cal = calendar.month(year, month)

    """Return the calendar as text"""
    return cal


"""Enter the year"""
year = int(input("Enter the year: "))

"""Enter the month number"""
month = int(input("Enter the month (1-12): "))

"""Call the function"""
result = generate_calendar(year, month)

"""Print the calendar"""
print(result)