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
