# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   6.14 LAB: Triangle pyramid area (part 2)
# Date:         23 September 2025

import math

side_length = float(input("Enter the side length in meters: "))
number_of_layers = int(input("Enter the number of layers: "))

# area of one small equilateral triangle (one prism's triangular face)
triangle_area = (math.sqrt(3) / 4) * side_length ** 2

# top area: large equilateral triangle made of n-by-n small triangles
top_area = triangle_area * (number_of_layers ** 2)

# each triangular prism has 3 rectangular side faces of area s * prism_height
# prism_height == side_length, so each rectangle area = s^2
# exposed rectangles along one pyramid edge = sum_{k=1..n} k = n(n+1)/2
one_edge_area = side_length ** 2 * (number_of_layers * (number_of_layers + 1) / 2)

# three sloping faces for the triangular-base pyramid
total_area = top_area + 3 * one_edge_area

# Output (base sits on ground, so bottom not covered)
print(f"You need {total_area:.2f} m^2 of gold foil to cover the pyramid")