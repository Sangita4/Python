# Write a Python program that prints the calendar for a given month and year.
# Note : Use 'calendar' module. 

import calendar
print(calendar.month(2024, 1))

y = int(input("Enter a year: "))
m = int(input("Enter a month: "))
print(calendar.month(y, m))
