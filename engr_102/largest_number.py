# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   Lab Topic 4 (individual)
# Date:         14 September 2025

number_1 = float(input('Enter number 1: '))
number_2 = float(input('Enter number 2: '))
number_3 = float(input('Enter number 3: '))

largest_number = number_1
# large comparison elif chain
if number_2 > largest_number:
    largest_number = number_2
if number_3 > largest_number:
    largest_number = number_3

print(f'The largest number is {largest_number}')