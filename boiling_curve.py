# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   Lab: Topic 5 (Individual)
# Date:         18 September 2025

from math import *

# Function for power-law interpolation
def power_law_interpolation(x, x0, y0, x1, y1):
    return y0 * ((x / x0) ** ((log10(y1 / y0) / log10(x1 / x0))))

# Get user input
excess_temperature = float(input('Enter the excess temperature: '))
# Assign x to the input value
x = excess_temperature

# Determine the surface heat flux based on the value of x
# Using piecewise power-law interpolation
# Region below 1.3
if x < 1.3:
    print('Surface heat flux is not available')
# Region 1.3 to 5
elif 1.3 <= x < 5:
    print(f'The surface heat flux is approximately {power_law_interpolation(x, 1.3, 1000, 5, 7000):.0f} W/m^2')
# Region 5 to 30
elif 5 <= x < 30:
    print(f'The surface heat flux is approximately {power_law_interpolation(x, 5, 7000, 30, 1.5e6):.0f} W/m^2')
# Region 30 to 120
elif 30 <= x < 120:
    print(f'The surface heat flux is approximately {power_law_interpolation(x, 30, 1.5e6, 120, 2.5e4):.0f} W/m^2')
# Region 120 to 1200
elif 120 <= x <= 1200:
    print(f'The surface heat flux is approximately {power_law_interpolation(x, 120, 2.5e4, 1200, 1.5e6):.0f} W/m^2')
# If x is greater than 1200
else:
    print('Surface heat flux is not available')