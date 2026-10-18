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

# """Import the calendar library"""
# import calendar
#
# """Create a function to generate a calendar"""
# def generate_calendar(year, month):
#     """Create the calendar for the given month and year"""
#     cal = calendar.month(year, month)
#
#     """Return the calendar as text"""
#     return cal
#
#
# """Enter the year"""
# year = int(input("Enter the year: "))
#
# """Enter the month number"""
# month = int(input("Enter the month (1-12): "))
#
# """Call the function"""
# result = generate_calendar(year, month)
#
# """Print the calendar"""
# print(result)



#Об'єктно-орієнтоване програмування
#Тема: Класи. Об'єкти. Частина 1


#Завдання 1
# class Car:
#     def __init__(self, model, year, manufacturer, engine, color, price):
#         self.model = model
#         self.year = year
#         self.manufacturer = manufacturer
#         self.engine = engine
#         self.color = color
#         self.price = price
#
#     # Method to display information about the car
#     def show_info(self):
#         print("Car model:", self.model)
#         print("Year:", self.year)
#         print("Manufacturer:", self.manufacturer)
#         print("Engine volume:", self.engine, "L")
#         print("Color:", self.color)
#         print("Price:", self.price, "UAH")
#
#     # Method to change the price
#     def change_price(self, new_price):
#         self.price = new_price
#         print("Car price has been changed.")
#
#     # Method to change the color
#     def change_color(self, new_color):
#         self.color = new_color
#         print("Car color has been changed.")
#
#
# # Create an object of the Car class
# car1 = Car("BMW X5", 2020, "BMW", 3.0, "Black", 1500000)
#
# # Display car information
# car1.show_info()
#
# print()
#
# # Change the car price
# car1.change_price(1400000)
#
# # Change the car color
# car1.change_color("White")
#
# print()
#
# # Display updated car information
# car1.show_info()



# #Завдання 2
# class Book:
#     """Class that stores information about a book."""
#
#     def __init__(self, title, year, publisher, genre, author, price):
#         """Initialize the book attributes."""
#         self.title = title
#         self.year = year
#         self.publisher = publisher
#         self.genre = genre
#         self.author = author
#         self.price = price
#
#     def show_info(self):
#         """Display information about the book."""
#         print("Book title:", self.title)
#         print("Year of publication:", self.year)
#         print("Publisher:", self.publisher)
#         print("Genre:", self.genre)
#         print("Author:", self.author)
#         print("Price:", self.price, "UAH")
#
#     def change_price(self, new_price):
#         """Change the price of the book."""
#         self.price = new_price
#         print("Book price has been changed.")
#
#     def change_genre(self, new_genre):
#         """Change the genre of the book."""
#         self.genre = new_genre
#         print("Book genre has been changed.")
#
#
# """Create an object of the Book class."""
# book1 = Book("Dune", 1965, "Chilton Books", "Science Fiction",
#              "Frank Herbert", 500)
#
# """Display book information."""
# book1.show_info()
#
# print()
#
# """Change the book price."""
# book1.change_price(550 )
#
# """Change the book genre."""
# book1.change_genre("Science Fiction")
# print()
# """Display updated book information."""
# book1.show_info()



# Об'єктно-орієнтоване програмування
# Тема: Статичні методи. Частина 3
#
#
# Завдання 1

class Fraction:
    """
    A class for working with fractions.
    """

    count = 0

    def __init__(self, numerator, denominator):
        """
        Initializes a fraction and increases the object counter.
        """
        self.numerator = numerator
        self.denominator = denominator
        Fraction.count += 1

    @staticmethod
    def count_objects():
        """
        Returns the number of created Fraction objects.
        """
        return Fraction.count


# Create fraction objects
fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)
fraction3 = Fraction(5, 6)

# Display the number of created objects
print("Number of created fractions:", Fraction.count_objects())
















