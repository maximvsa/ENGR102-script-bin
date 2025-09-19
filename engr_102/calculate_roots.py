# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   Lab: Topic 4 (individual)
# Date:         14 September 2025

from math import *

complex = False

coefficient_a = float(input('Please enter the coefficient A: '))
coefficient_b = float(input('Please enter the coefficient B: '))
coefficient_c = float(input('Please enter the coefficient C: '))

discriminant = (coefficient_b ** 2) - (4 * coefficient_a * coefficient_c)
if discriminant < 0:
    complex = True
    discriminant = abs(discriminant)

# textbook quadratic "function"
def root_cracker():
    root_1 = (-coefficient_b + sqrt(discriminant)) / (2 * coefficient_a)
    root_2 = (-coefficient_b - sqrt(discriminant)) / (2 * coefficient_a)
    return root_1, root_2

if not complex:
    if coefficient_a != 0:
        if max(root_cracker()) == min(root_cracker()):
            print(f'The root is x = {root_cracker()[0]}')
        else:
            print(f'The roots are x = {max(root_cracker())} and x = {min(root_cracker())}')
    elif coefficient_a == coefficient_b == 0:
        if coefficient_c == 0:
            print('something')
        else:
            print('You entered an invalid combination of coefficients!')
    elif coefficient_a == 0:
        print(f'The root is x = {(-coefficient_c) / coefficient_b}')
else:
    real_component = (-coefficient_b) / (2 * coefficient_a)
    imaginary_component = sqrt(discriminant) / (2 * coefficient_a)
    if max(root_cracker()) == min(root_cracker()):
        print(f'The root is x = {real_component} + {imaginary_component}i')
    else:
        print(f'The roots are x = {real_component} + {imaginary_component}i and x = {real_component} - {imaginary_component}i')