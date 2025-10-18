# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   9.17 LAB: Double factorial
# Date:         18 October 2025

def doublefactorial(input_number):
    product = 1
    # Comment
    for i in range(input_number, 0, -2):
        product *= i
    return product