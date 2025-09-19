# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   4.13 LAB: Nominal diameter
# Date:         13 September 2025

nominal_bolt_diameter = float(input('Enter the nominal diameter: '))
actual_bolt_diameter = float(input('Enter the actual diameter: '))

# relative change formula
percent_difference = (abs(nominal_bolt_diameter - actual_bolt_diameter) / actual_bolt_diameter) * 100

# elif chain to branch
if percent_difference < 1:
    print('The diameter is within <1% of desired value')
elif 1 <= percent_difference < 2:
    print('The diameter is between 1% and <2% of desired value')
elif 2 <= percent_difference < 5:
    print('The diameter is between 2% and <5% of desired value')
else:
    print('Out of specifications, >=5% error')
