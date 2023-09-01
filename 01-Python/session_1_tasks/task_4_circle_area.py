#!/usr/bin/python3

#------------------------------------------------------------------------------------------------
# Write a Python program which accepts the radius of a circle from the user and compute the area.
#------------------------------------------------------------------------------------------------

from math import pi
r = float (input("Enter Radius of Circle in cm : "))
print("The Area of circle = " + str(pi * r**2) + " Cm\u00b2")