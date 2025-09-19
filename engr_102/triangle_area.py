# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   3.17 LAB: Triangle area
# Date:         11 September 2025

from math import *

side_length_x = float(input('Enter the value of x: '))
side_length_y = float(input('Enter the value of y: '))

side_a = sqrt(2) * side_length_y
side_b = sqrt((side_length_y ** 2) - (2 * side_length_y * side_length_x) + (2 * (side_length_x ** 2)))
side_c = sqrt((side_length_y ** 2) + (2 * side_length_y * side_length_x) + (2 * (side_length_x ** 2)))

semiperimeter = 0.5 * (side_a + side_b + side_c)

# Heron's formula
triangle_area = sqrt(semiperimeter * (semiperimeter - side_a) * (semiperimeter - side_b) * (semiperimeter - side_c))

print(f'The area of the triangle is {triangle_area:.3f}')