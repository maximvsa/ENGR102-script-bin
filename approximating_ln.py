# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   6.15 LAB: Approximating ln
# Date:         23 September 2025

import math

user_x = float(input("Enter a value for x: "))

while user_x <= 0 or user_x > 2:
    user_x = float(input('Out of range! Try again: '))

tolerance = float(input("Enter the tolerance: "))

approximation = 0
for i in range(0, 999999):
    next_term = ((-1) ** i) * ((user_x - 1) ** (i + 1)) / (i + 1)

# check to see if tolerance has been reached
    if abs(next_term) < tolerance:
        break
    approximation += next_term
print(f'ln({user_x}) is approximately {float(approximation)}')
print(f'ln({user_x}) is exactly {math.log(user_x)}')
print(f'The difference is {abs(approximation - math.log(user_x))}')