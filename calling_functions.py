# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   Lab: Topic 3 (Individual)
# Date:         9 September 2025

from math import *

def printresult(shape, side, area):
    '''Print the result of the calculation'''
    print(f'A {shape} with side {side:.2f} has area {area:.3f}')

# example function call:
# printresult(<string of shape name>, <float of side>, <float of area>)
# printresult('square', 2.236, 5)
# Your code goes here

side_length = float(input('Please enter the side length: '))
printresult('triangle', side_length, (sqrt(3) / 4) * (side_length ** 2))
printresult('square', side_length, side_length ** 2)
printresult('pentagon', side_length, (0.25) * (sqrt(5 * (5 + (2 * sqrt(5))))) * (side_length ** 2))
printresult('hexagon', side_length, (1.5) * (sqrt(3) * (side_length ** 2)))
printresult('dodecagon', side_length, 3 * (2 + sqrt(3)) * (side_length ** 2))