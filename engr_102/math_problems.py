# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   3.18 LAB: Math problems
# Date:         11 September 2025

from math import *

print("Part 1")

door_height = float(input('Enter the height of the door: '))
door_width = float(input('Enter the width of the door: '))

door_arc_radius = door_width / sqrt(2)

# arc saggita formula
door_arc_saggita = door_width * ((1 / sqrt(2)) - 0.5)
rectangle_area = door_width * (door_height - door_arc_saggita)
door_arc_saggita_area = ((door_width ** 2) / 8) * (pi - 2)
door_area = rectangle_area + door_arc_saggita_area

print(f'The area of the door is {door_area:.2f}')

print('Part 2')
pyramid_height = float(input('Enter the height of the pyramid: '))

# pyramid surface area in terms of height formula
print(f'The surface area of the pyramid is {2 * (pyramid_height ** 2) * (1 + sqrt(3)):.2f}')

print('Part 3')
triangle_area = float(input('Enter the area of a triangle: '))

# inverse formula for finding the area of an equilateral triangle given the length of any side
side_a_length = sqrt((4 / sqrt(3)) * triangle_area)
print(f'The equilateral triangle has sides with length {side_a_length:.2f}')

# formula for solving the length of the base of an isosceles triangle given the other side length and area
side_b_length = sqrt(2 * (side_a_length ** 2) + 2 * sqrt((side_a_length ** 4) - (4 * (triangle_area ** 2))))
print(f'The isosceles triangle has two sides with lengths {side_a_length:.2f} and one side with length {side_b_length:.2f}')

side_c_length = (2 * triangle_area) / side_b_length
# pythagorean theorem
side_d_length = sqrt((side_b_length ** 2) + (side_c_length ** 2))
print(f'The right triangle has sides with lengths {side_b_length:.2f}, {side_c_length:.2f}, and {side_d_length:.2f}')

# heron's formula
arbitrary_triangle_semiperimeter = (2 * triangle_area) / (side_a_length * side_d_length)
side_e_length = sqrt((side_a_length ** 2) + (side_d_length ** 2) - (2 * side_a_length * side_d_length * sqrt(1 - (arbitrary_triangle_semiperimeter ** 2))))
print(f'The arbitrary triangle has sides with lengths {side_a_length:.2f}, {side_d_length:.2f}, and {side_e_length:.2f}')