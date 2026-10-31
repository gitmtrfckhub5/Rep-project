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
#
# class Fraction:
#     """
#     A class for working with fractions.
#     """
#
#     count = 0
#
#     def __init__(self, numerator, denominator):
#         """
#         Initializes a fraction and increases the object counter.
#         """
#         self.numerator = numerator
#         self.denominator = denominator
#         Fraction.count += 1
#
#     @staticmethod
#     def count_objects():
#         """
#         Returns the number of created Fraction objects.
#         """
#         return Fraction.count
#
#
# # Create fraction objects
# fraction1 = Fraction(1, 2)
# fraction2 = Fraction(3, 4)
# fraction3 = Fraction(5, 6)
#
# # Display the number of created objects
# print("Number of created fractions:", Fraction.count_objects())


# Завдання 2
#
# class Temperature:
#     """
#     A class for converting temperatures.
#     """
#
#     count = 0
#
#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         """
#         Converts Celsius to Fahrenheit.
#         """
#         Temperature.count += 1
#         return celsius * 9 / 5 + 32
#
#     @staticmethod
#     def fahrenheit_to_celsius(fahrenheit):
#         """
#         Converts Fahrenheit to Celsius.
#         """
#         Temperature.count += 1
#         return (fahrenheit - 32) * 5 / 9
#
#     @staticmethod
#     def count_calculations():
#         """
#         Returns the number of temperature calculations.
#         """
#         return Temperature.count
#
#
# # Convert Celsius to Fahrenheit
# result1 = Temperature.celsius_to_fahrenheit(25)
# print("25 Celsius =", result1, "Fahrenheit")
#
# # Convert Fahrenheit to Celsius
# result2 = Temperature.fahrenheit_to_celsius(77)
# print("77 Fahrenheit =", result2, "Celsius")
#
# # Display the number of calculations
# print("Number of calculations:", Temperature.count_calculations())

# Завдання 3
#
# class LengthConverter:
#     """
#     A class for converting units of length.
#     """
#
#     @staticmethod
#     def meters_to_feet(meters):
#         """
#         Converts meters to feet.
#         """
#         return meters * 3.28084
#
#     @staticmethod
#     def feet_to_meters(feet):
#         """
#         Converts feet to meters.
#         """
#         return feet / 3.28084
#
#
# # Convert meters to feet
# meters = 10
# result1 = LengthConverter.meters_to_feet(meters)
# print(meters, "meters =", round(result1, 2), "feet")
#
# # Convert feet to meters
# feet = 20
# result2 = LengthConverter.feet_to_meters(feet)
# print(feet, "feet =", round(result2, 2), "meters")




#Тема: Успадкування. Частина 1
 #Завдання 1
#
#
# class Device:
#     """Class that stores information about a device."""
#
#     def __init__(self, name, brand, power):
#         """Initialize the device."""
#         self.name = name
#         self.brand = brand
#         self.power = power
#
#     def show_info(self):
#         """Display information about the device."""
#         print("Device name:", self.name)
#         print("Brand:", self.brand)
#         print("Power:", self.power, "W")
#
#
# class CoffeeMachine(Device):
#     """Class that describes a coffee machine."""
#
#     def __init__(self, name, brand, power, coffee_type):
#         """Initialize the coffee machine."""
#         super().__init__(name, brand, power)
#         self.coffee_type = coffee_type
#
#     def make_coffee(self):
#         """Make coffee."""
#         print("The coffee machine is making:", self.coffee_type)
#
#
# class Blender(Device):
#     """Class that describes a blender."""
#
#     def __init__(self, name, brand, power, speed):
#         """Initialize the blender."""
#         super().__init__(name, brand, power)
#         self.speed = speed
#
#     def blend(self):
#         """Start the blender."""
#         print("The blender is working at speed:", self.speed)
#
#
# class MeatGrinder(Device):
#     """Class that describes a meat grinder."""
#
#     def __init__(self, name, brand, power, productivity):
#         """Initialize the meat grinder."""
#         super().__init__(name, brand, power)
#         self.productivity = productivity
#
#     def grind_meat(self):
#         """Grind meat."""
#         print("The meat grinder is grinding meat.")
#         print("Productivity:", self.productivity, "kg/min")
#
#
# """Create objects."""
#
# coffee_machine = CoffeeMachine(
#     "Coffee Machine", "Philips", 1500, "cappuccino"
# )
#
# blender = Blender(
#     "Blender", "Bosch", 800, 3
# )
#
# meat_grinder = MeatGrinder(
#     "Meat Grinder", "Moulinex", 1200, 2
# )
#
#
# """Display information about the coffee machine."""
#
# print("Coffee Machine:")
# coffee_machine.show_info()
# coffee_machine.make_coffee()
#
# print()
#
#
# """Display information about the blender."""
#
# print("Blender:")
# blender.show_info()
# blender.blend()
#
# print()
#
#
# """Display information about the meat grinder."""
#
# print("Meat Grinder:")
# meat_grinder.show_info()
# meat_grinder.grind_meat()


#Тема: Успадкування. Частина 1
#Завдання 2

#
# class Ship:
#     """Class that stores information about a ship."""
#
#     def __init__(self, name, country, speed):
#         """Initialize the ship."""
#         self.name = name
#         self.country = country
#         self.speed = speed
#
#     def show_info(self):
#         """Display information about the ship."""
#         print("Ship name:", self.name)
#         print("Country:", self.country)
#         print("Speed:", self.speed, "knots")
#
#
# class Frigate(Ship):
#     """Class that describes a frigate."""
#
#     def __init__(self, name, country, speed, missiles):
#         """Initialize the frigate."""
#         super().__init__(name, country, speed)
#         self.missiles = missiles
#
#     def patrol(self):
#         """Start patrolling."""
#         print("The frigate", self.name, "is patrolling.")
#         print("Number of missiles:", self.missiles)
#
#
# class Destroyer(Ship):
#     """Class that describes a destroyer."""
#
#     def __init__(self, name, country, speed, guns):
#         """Initialize the destroyer."""
#         super().__init__(name, country, speed)
#         self.guns = guns
#
#     def attack(self):
#         """Show information about the destroyer's weapons."""
#         print("The destroyer", self.name, "is ready for action.")
#         print("Number of guns:", self.guns)
#
#
# class Cruiser(Ship):
#     """Class that describes a cruiser."""
#
#     def __init__(self, name, country, speed, crew):
#         """Initialize the cruiser."""
#         super().__init__(name, country, speed)
#         self.crew = crew
#
#     def show_crew(self):
#         """Display the number of crew members."""
#         print("The cruiser", self.name, "has", self.crew, "crew members.")
#
#
# """Create objects."""
#
# frigate = Frigate("Brees", "USA", 29, 16)
# destroyer = Destroyer("Arleigh Burke", "USA", 30, 5)
#
# cruiser = Cruiser("Ticonderoga", "USA", 32, 400)
#
#
# """Display information about the frigate."""
#
# print("Frigate:")
# frigate.show_info()
# frigate.patrol()
#
# print()
#
#
# """Display information about the destroyer."""
#
# print("Destroyer:")
# destroyer.show_info()
# destroyer.attack()
#
# print()
#
#
# """Display information about the cruiser."""
#
# print("Cruiser:")
# cruiser.show_info()
# cruiser.show_crew()



# Тема: Множинне успадкування. Поліморфізм. Реалізація магічних методів.
# Завдання 1
#
#
#
# import math
#
#
# class Figure:
#     """Base class for figures."""
#
#     def area(self):
#         """Calculate the area of a figure."""
#         return 0
#
#     def __str__(self):
#         """Return the area of a figure."""
#         return "Area: " + str(round(self.area(), 2))
#
#
# class Rectangle(Figure):
#     """Class for a rectangle."""
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         """Calculate the rectangle area."""
#         return self.width * self.height
#
#
# class Circle(Figure):
#     """Class for a circle."""
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         """Calculate the circle area."""
#         return math.pi * self.radius ** 2
#
#
# class RightTriangle(Figure):
#     """Class for a right triangle."""
#
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#
#     def area(self):
#         """Calculate the right triangle area."""
#         return self.base * self.height / 2
#
#
# class Trapezoid(Figure):
#     """Class for a trapezoid."""
#
#     def __init__(self, base1, base2, height):
#         self.base1 = base1
#         self.base2 = base2
#         self.height = height
#
#     def area(self):
#         """Calculate the trapezoid area."""
#         return (self.base1 + self.base2) * self.height / 2
#
#
# """Create figure objects."""
#
# rectangle = Rectangle(5, 4)
# circle = Circle(3)
# triangle = RightTriangle(6, 4)
# trapezoid = Trapezoid(5, 7, 4)
#
#
# """Display the areas of the figures."""
#
# print("Rectangle:", rectangle)
# print("Circle:", circle)
# print("Right triangle:", triangle)
# print("Trapezoid:", trapezoid)
#


# Завдання 2

#
# import math
#
#
# class Figure:
#     """Base class for figures."""
#
#     def area(self):
#         """Calculate the area of a figure."""
#         return 0
#
#     def __int__(self):
#         """Return the area as an integer."""
#         return int(self.area())
#
#     def __str__(self):
#         """Return information about the figure."""
#         return "Figure. Area: " + str(round(self.area(), 2))
#
#
# class Rectangle(Figure):
#     """Class for a rectangle."""
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         """Calculate the rectangle area."""
#         return self.width * self.height
#
#     def __str__(self):
#         return "Rectangle. Width: " + str(self.width) + \
#                ", height: " + str(self.height) + \
#                ", area: " + str(round(self.area(), 2))
#
#
# class Circle(Figure):
#     """Class for a circle."""
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         """Calculate the circle area."""
#         return math.pi * self.radius ** 2
#
#     def __str__(self):
#         return "Circle. Radius: " + str(self.radius) + \
#                ", area: " + str(round(self.area(), 2))
#
#
# class RightTriangle(Figure):
#     """Class for a right triangle."""
#
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#
#     def area(self):
#         """Calculate the triangle area."""
#         return self.base * self.height / 2
#
#     def __str__(self):
#         return "Right triangle. Base: " + str(self.base) + \
#                ", height: " + str(self.height) + \
#                ", area: " + str(round(self.area(), 2))
#
#
# class Trapezoid(Figure):
#     """Class for a trapezoid."""
#
#     def __init__(self, base1, base2, height):
#         self.base1 = base1
#         self.base2 = base2
#         self.height = height
#
#     def area(self):
#         """Calculate the trapezoid area."""
#         return (self.base1 + self.base2) * self.height / 2
#
#     def __str__(self):
#         return "Trapezoid. Bases: " + str(self.base1) + \
#                " and " + str(self.base2) + \
#                ", height: " + str(self.height) + \
#                ", area: " + str(round(self.area(), 2))
#
#
# """Create figure objects."""
#
# rectangle = Rectangle(5, 4)
# circle = Circle(3)
# triangle = RightTriangle(6, 4)
# trapezoid = Trapezoid(5, 7, 4)
#
#
# """Display information about the figures."""
#
# print(rectangle)
# print("Integer area:", int(rectangle))
# print()
#
# print(circle)
# print("Integer area:", int(circle))
# print()
#
# print(triangle)
# print("Integer area:", int(triangle))
# print()
#
# print(trapezoid)
# print("Integer area:", int(trapezoid))


# Тема: Декоратори
# Завдання 1
#
#
#
# import time
#
#
# """Decorator for measuring the execution time of a function."""
# def timer(func):
#     def wrapper():
#         start = time.time()
#
#         result = func()
#
#         end = time.time()
#         print("Execution time:", round(end - start, 5), "seconds")
#
#         return result
#     return wrapper
#
#
# """Function for finding all prime numbers from 0 to 1000."""
# @timer
# def find_primes():
#     primes = []
#
#     for num in range(2, 1001):
#         is_prime = True
#
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break
#
#         if is_prime:
#             primes.append(num)
#
#     return primes
#
#
# """Call the function and print the prime numbers."""
# numbers = find_primes()
#
# print("Prime numbers from 0 to 1000:")
# print(numbers)



# Завдання 2

# import time
#
#
# """Decorator for measuring the execution time of a function."""
# def timer(func):
#     def wrapper(start_num, end_num):
#         start = time.time()
#
#         result = func(start_num, end_num)
#
#         end = time.time()
#         print("Execution time:", round(end - start, 5), "seconds")
#
#         return result
#     return wrapper
#
#
# """Function for finding prime numbers in a given range."""
# @timer
# def find_primes(start_num, end_num):
#     primes = []
#
#     for num in range(max(2, start_num), end_num + 1):
#         is_prime = True
#
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break
#
#         if is_prime:
#             primes.append(num)
#
#     return primes
#
#
# """Ask the user for the range boundaries."""
# start_num = int(input("Enter the start of the range: "))
# end_num = int(input("Enter the end of the range: "))
#
#
# """Call the function and print the prime numbers."""
# numbers = find_primes(start_num, end_num)
#
# print("Prime numbers:")
# print(numbers)


# Тема: Класи. Об'єкти. Конструктори. Перевантаження методів.
#
#
# Завдання 1

#
# class Car:
#     """Constructor of the Car class."""
#     def __init__(self, model, year, manufacturer, engine, color, price):
#         self.model = model
#         self.year = year
#         self.manufacturer = manufacturer
#         self.engine = engine
#         self.color = color
#         self.price = price
#
#     """Method to display car information."""
#     def show_info(self):
#         print("Car model:", self.model)
#         print("Year:", self.year)
#         print("Manufacturer:", self.manufacturer)
#         print("Engine volume:", self.engine, "L")
#         print("Color:", self.color)
#         print("Price:", self.price, "UAH")
#
#     """Method to change the price."""
#     def change_price(self, new_price=None):
#         if new_price is not None:
#             self.price = new_price
#         print("Price:", self.price, "UAH")
#
#     """Method to change the color."""
#     def change_color(self, new_color=None):
#         if new_color is not None:
#             self.color = new_color
#         print("Color:", self.color)
#
#
# # Create a car object
# car1 = Car("BMW X5", 2020, "BMW", 3.0, "Black", 1500000)
#
# # Display car information
# car1.show_info()
#
# print()
#
# # Change price and color
# car1.change_price(1400000)
# car1.change_color("White")
#
# print()
#
# # Display updated information
# car1.show_info()
#
# print()
#
# # Call methods without arguments
# car1.change_price()
# car1.change_color()


# Завдання 2
#
#
#
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
#     """Display information about the book."""
#     def show_info(self):
#         print("Book title:", self.title)
#         print("Year of publication:", self.year)
#         print("Publisher:", self.publisher)
#         print("Genre:", self.genre)
#         print("Author:", self.author)
#         print("Price:", self.price, "UAH")
#
#     """Change the price of the book."""
#     def change_price(self, new_price=None):
#         if new_price is not None:
#             self.price = new_price
#         print("Price:", self.price, "UAH")
#
#     """Change the genre of the book."""
#     def change_genre(self, new_genre=None):
#         if new_genre is not None:
#             self.genre = new_genre
#         print("Genre:", self.genre)
#
#
# """Create a book object."""
# book1 = Book("Dune", 1965, "Chilton Books",
#              "Science Fiction", "Frank Herbert", 500)
#
# """Display book information."""
# book1.show_info()
#
# print()
#
# """Change the book price and genre."""
# book1.change_price(550)
# book1.change_genre("Adventure")
#
# print()
#
# """Display updated book information."""
# book1.show_info()
#
# print()
#
# """Call methods without arguments."""
# book1.change_price()
# book1.change_genre()


# Тема: Перевантаження операторів.


# Завдання 1
#
#
# class Circle:
#     """Class that stores information about a circle."""
#
#     def __init__(self, radius):
#         """Initialize the circle radius."""
#         self.radius = radius
#
#     """Compare two circles by radius."""
#     def __eq__(self, other):
#         return self.radius == other.radius
#
#     """Compare two circles by circumference."""
#     def __gt__(self, other):
#         return self.radius > other.radius
#
#     def __lt__(self, other):
#         return self.radius < other.radius
#
#     def __le__(self, other):
#         return self.radius <= other.radius
#
#     def __ge__(self, other):
#         return self.radius >= other.radius
#
#     """Increase the circle radius."""
#     def __add__(self, value):
#         return Circle(self.radius + value)
#
#     """Decrease the circle radius."""
#     def __sub__(self, value):
#         return Circle(self.radius - value)
#
#     """Increase the radius of the current circle."""
#     def __iadd__(self, value):
#         self.radius += value
#         return self
#
#     """Decrease the radius of the current circle."""
#     def __isub__(self, value):
#         self.radius -= value
#         return self
#
#     """Display the circle radius."""
#     def show_info(self):
#         print("Circle radius:", self.radius)
#
#
# """Create two circle objects."""
# circle1 = Circle(5)
# circle2 = Circle(3)
#
# """Compare the circles."""
# print("Circles are equal:", circle1 == circle2)
# print("Circle1 > Circle2:", circle1 > circle2)
# print("Circle1 < Circle2:", circle1 < circle2)
# print("Circle1 <= Circle2:", circle1 <= circle2)
# print("Circle1 >= Circle2:", circle1 >= circle2)
#
# print()
#
# """Change the radius using plus and minus operators."""
# circle3 = circle1 + 2
# circle4 = circle1 - 1
#
# circle3.show_info()
# circle4.show_info()
#
# print()
#
# """Change the radius using += and -= operators."""
# circle1 += 3
# circle1.show_info()
#
# circle1 -= 2
# circle1.show_info()


# Завдання 2
#
# class Complex:
#     """Class for working with complex numbers."""
#
#     """Constructor of the Complex class."""
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag
#
#     """Addition of two complex numbers."""
#     def __add__(self, other):
#         return Complex(
#             self.real + other.real,
#             self.imag + other.imag
#         )
#
#     """Subtraction of two complex numbers."""
#     def __sub__(self, other):
#         return Complex(
#             self.real - other.real,
#             self.imag - other.imag
#         )
#
#     """Multiplication of two complex numbers."""
#     def __mul__(self, other):
#         real = self.real * other.real - self.imag * other.imag
#         imag = self.real * other.imag + self.imag * other.real
#         return Complex(real, imag)
#
#     """Division of two complex numbers."""
#     def __truediv__(self, other):
#         denominator = other.real ** 2 + other.imag ** 2
#
#         if denominator == 0:
#             print("Division by zero is not allowed.")
#             return None
#
#         real = (self.real * other.real +
#                 self.imag * other.imag) / denominator
#
#         imag = (self.imag * other.real -
#                 self.real * other.imag) / denominator
#
#         return Complex(real, imag)
#
#     """Display the complex number."""
#     def show_info(self):
#         print(f"{self.real} + ({self.imag})i")
#
#
# """Create two complex numbers."""
# num1 = Complex(4, 3)
# num2 = Complex(2, 1)
#
# """Perform arithmetic operations."""
# result = num1 + num2
# print("Addition:")
# result.show_info()
#
# result = num1 - num2
# print("Subtraction:")
# result.show_info()
#
# result = num1 * num2
# print("Multiplication:")
# result.show_info()
#
# result = num1 / num2
# print("Division:")
# if result is not None:
#     result.show_info()



#
# class BankAccount:
#     """This class describes a bank account."""
#
#     def __init__(self, owner, balance):
#         """Create a new bank account."""
#         self.owner = owner
#         self.__balance = balance
#
#     @property
#     def balance(self):
#         """Return the current balance."""
#         return self.__balance
#
#     def deposit(self, amount):
#         """Add money to the account."""
#         if amount > 0:
#             self.__balance += amount
#             print("Money successfully deposited")
#         else:
#             print("Amount must be greater than zero")
#
#     def withdraw(self, amount):
#         """Withdraw money from the account."""
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -= amount
#             print("Money successfully withdrawn")
#         else:
#             print("Not enough money or incorrect amount")
#
#     def change_balance(self, amount):
#         """Change the account balance."""
#         self.__balance += amount
#
#     def __str__(self):
#         """Return information about the account."""
#         return f"Owner: {self.owner}, Balance: {self.balance}"
#
#
# class SavingsAccount(BankAccount):
#     """This class describes a savings account."""
#
#     def __init__(self, owner, balance, interest_rate):
#         """Create a savings account."""
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate
#
#     def add_interest(self):
#         """Add interest to the account balance."""
#         interest = self.balance * self.interest_rate / 100
#         self.change_balance(interest)
#         print(f"Interest added: {interest}")
#
#     def withdraw(self, amount):
#         """Withdraw money from a savings account."""
#         if amount > 0 and amount <= self.balance:
#             self.change_balance(-amount)
#             print("Money withdrawn from savings account")
#         else:
#             print("Not enough money")
#
#     def __str__(self):
#         """Return information about the savings account."""
#         return (f"Savings Account. Owner: {self.owner}, "
#                 f"Balance: {self.balance}, Interest: {self.interest_rate}%")
#
#
# class BusinessAccount(BankAccount):
#     """This class describes a business account."""
#
#     def __init__(self, owner, balance, commission):
#         """Create a business account."""
#         super().__init__(owner, balance)
#         self.commission = commission
#
#     def withdraw(self, amount):
#         """Withdraw money with a commission."""
#         total = amount + self.commission
#
#         if amount > 0 and total <= self.balance:
#             self.change_balance(-total)
#             print(f"Money withdrawn. Commission: {self.commission}")
#         else:
#             print("Not enough money including commission")
#
#     def __str__(self):
#         """Return information about the business account."""
#         return (f"Business Account. Owner: {self.owner}, "
#                 f"Balance: {self.balance}, Commission: {self.commission}")
#
#
# # Testing the program
#
# account1 = BankAccount("David", 1000)
# print(account1)
#
# account1.deposit(500)
# account1.withdraw(200)
# print(account1)
#
# print("-------------------------")
#
# account2 = SavingsAccount("Anna", 2000, 5)
# print(account2)
#
# account2.add_interest()
# account2.withdraw(300)
# print(account2)
#
# print("-------------------------")
#
# account3 = BusinessAccount("Denis", 5000, 50)
# print(account3)
#
# account3.deposit(1000)
# account3.withdraw(500)
# print(account3)


# Завдання 2. Система обліку працівників


class Employee:
    """This class describes a company employee."""

    def __init__(self, name, employee_id, base_salary):
        """Create a new employee."""
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary

    def __calculate_bonus(self, percent):
        """Calculate employee bonus."""
        bonus = self.base_salary * percent / 100
        return bonus

    def calculate_salary(self):
        """Calculate total salary."""
        return self.base_salary + self.__calculate_bonus(5)

    def get_info(self):
        """Return employee information."""
        return (f"Name: {self.name}, "
                f"ID: {self.employee_id}, "
                f"Salary: {self.calculate_salary()}")

    @staticmethod
    def check_id(employee_id):
        """Check if employee ID is correct."""
        return employee_id.isdigit() and len(employee_id) == 4

    @classmethod
    def from_string(cls, data):
        """Create employee from a string."""
        name, employee_id, salary = data.split(",")
        return cls(name, employee_id, float(salary))


# Developer class
class Developer(Employee):
    """This class describes a developer."""

    def __init__(self, name, employee_id, base_salary, projects):
        super().__init__(name, employee_id, base_salary)
        self.projects = projects

    def calculate_salary(self):
        """Calculate developer salary."""
        bonus = self.base_salary * 10 / 100
        return self.base_salary + bonus + self.projects * 100


# Manager class
class Manager(Employee):
    """This class describes a manager."""

    def __init__(self, name, employee_id, base_salary, team_size):
        super().__init__(name, employee_id, base_salary)
        self.team_size = team_size

    def calculate_salary(self):
        """Calculate manager salary."""
        bonus = self.base_salary * 15 / 100
        return self.base_salary + bonus + self.team_size * 200


# Designer class
class Designer(Employee):
    """This class describes a designer."""

    def __init__(self, name, employee_id, base_salary, experience):
        super().__init__(name, employee_id, base_salary)
        self.experience = experience

    def calculate_salary(self):
        """Calculate designer salary."""
        bonus = self.base_salary * 8 / 100
        return self.base_salary + bonus + self.experience * 150


# TeamLead class
class TeamLead(Developer, Manager):
    """This class describes a team leader."""

    def __init__(self, name, employee_id, base_salary,
                 projects, team_size):
        Employee.__init__(self, name, employee_id, base_salary)
        self.projects = projects
        self.team_size = team_size

    def calculate_salary(self):
        """Calculate team leader salary."""
        bonus = self.base_salary * 20 / 100
        return (self.base_salary + bonus
                + self.projects * 100
                + self.team_size * 200)


# Testing the program

employee1 = Developer("Alex", "1001", 3000, 5)
employee2 = Manager("Den", "1002", 4000, 4)
employee3 = Designer("David", "1003", 2500, 3)
employee4 = TeamLead("Emma", "1004", 5000, 6, 5)

# Create a list of employees
employees = [employee1, employee2, employee3, employee4]

# Print information about all employees
for employee in employees:
    print(employee.get_info())

print("-------------------------")

# Check employee ID
print("ID 1001:", Employee.check_id("1001"))
print("ID 123:", Employee.check_id("123"))

print("-------------------------")

# Create employee from a string
new_employee = Employee.from_string("Andrii,1005,3500")
print(new_employee.get_info())

print("-------------------------")

# Show MRO
print("TeamLead MRO:")
print(TeamLead.mro())

print("-------------------------")

# Calculate salary for all employees
for employee in employees:
    print(employee.name, "Salary:", employee.calculate_salary())