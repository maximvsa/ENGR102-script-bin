# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   9.16 LAB: Writing functions
# Date:         18 October 2025

import math

def triangle_area(side_length):
    area = (math.sqrt(3) / 4) * side_length**2
    print(f"A triangle with side {side_length:.2f} has area {area:.3f}")

def square_area(side_length):
    area = side_length**2
    print(f"A square with side {side_length:.2f} has area {area:.3f}")

def pentagon_area(side_length):
    area = (1/4) * (math.sqrt(5 * (5 + 2 * math.sqrt(5)))) * side_length**2
    print(f"A pentagon with side {side_length:.2f} has area {area:.3f}")

def hexagon_area(side_length):
    area = (3/2) * math.sqrt(3) * side_length**2
    print(f"A hexagon with side {side_length:.2f} has area {area:.3f}")

def dodecagon_area(side_length):
    area = 3 * (2 + math.sqrt(3)) * side_length**2
    print(f"A dodecagon with side {side_length:.2f} has area {area:.3f}")

# Comment
side_length = float(input("Please enter the side length: "))

triangle_area(side_length)
square_area(side_length)
pentagon_area(side_length)
hexagon_area(side_length)
dodecagon_area(side_length)