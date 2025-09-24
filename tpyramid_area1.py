# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   6.13 LAB: Triangle pyramid area (part 1)
# Date:         23 September 2025

import math

side_length = float(input("Enter the side length in meters: "))
number_of_layers = int(input("Enter the number of layers: "))

# area of one small equilateral triangle
triangle_area = (math.sqrt(3) / 4) * side_length ** 2

# total top area = area of large equilateral triangle subdivided into n^2 small ones
top_area = triangle_area * (number_of_layers ** 2)

# for loop to sum exposed rectangles along one pyramid edge
one_edge_area = 0
for k in range(1, number_of_layers + 1):
    one_edge_area += k * (side_length ** 2)

# three sloping edges for a triangular base pyramid
total_area = top_area + 3 * one_edge_area

# Output the total area needed to cover the pyramid (base sits on ground, so bottom not covered)
print(f"You need {total_area:.2f} m^2 of gold foil to cover the pyramid")