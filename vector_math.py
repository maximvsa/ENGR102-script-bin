# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   7.16 LAB: Vector math
# Date:         1 October 2025

import math

vector_a_element_string = input("Enter the elements for vector A: ")
vector_a_element_list = vector_a_element_string.split()
vector_a_element_list = [float(element) for element in vector_a_element_list]

vector_b_element_string = input("Enter the elements for vector B: ")
vector_b_element_list = vector_b_element_string.split()
vector_b_element_list = [float(element) for element in vector_b_element_list]

# Vector A magnitude calculation block
vector_a_square_sum = 0
for element in vector_a_element_list:
    vector_a_square_sum += element ** 2
vector_a_magnitude = math.sqrt(vector_a_square_sum)
print(f"The magnitude of vector A is {vector_a_magnitude:.5f}")

# Vector B magnitude calculation block
vector_b_square_sum = 0
for element in vector_b_element_list:
    vector_b_square_sum += element ** 2
vector_b_magnitude = math.sqrt(vector_b_square_sum)
print(f"The magnitude of vector B is {vector_b_magnitude:.5f}")

print(f"A + B is {[vector_a_element_list[element] + vector_b_element_list[element] for element in range(len(vector_a_element_list))]}")
print(f"A - B is {[vector_a_element_list[element] - vector_b_element_list[element] for element in range(len(vector_a_element_list))]}")

vector_a_b_dp = 0
for element in range(len(vector_a_element_list)):
    vector_a_b_dp += vector_a_element_list[element] * vector_b_element_list[element]

print(f"The dot product is {vector_a_b_dp:.2f}")