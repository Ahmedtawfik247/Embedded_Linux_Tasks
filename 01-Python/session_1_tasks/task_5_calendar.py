#!/usr/bin/python3

#----------------------------------------------
# Print the calendar of a given month and year.
#----------------------------------------------

import calendar
y = int(input("Enter The year :"))
m = int(input("Enter The month :"))
print(calendar.month(y,m))