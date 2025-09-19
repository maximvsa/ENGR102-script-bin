# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   Lab: Topic 4 (individual)
# Date:         14 September 2025

day = int(input('Please enter a positive value for day: '))

# summation series python equivalent
def sigma(lower_bound, upper_bound):
    if lower_bound > upper_bound:
        return 0
    iteration = upper_bound - lower_bound + 1
    return (upper_bound + lower_bound) * iteration // 2

try:
    if day < 0:
        print('You entered an invalid number!')
    else:
        if day < 11:
            gadgets_produced = 10 * day
        elif 11 <= day <= 50:
            gadgets_produced = 100 + sigma(11, day)
        elif 50 < day < 101:
            gadgets_produced = 100 + sigma(11, 50) + 50 * (day - 50)
        elif day >= 101:
            gadgets_produced = 3820
        print(f'The sum total number of gadgets produced on day {day} is {gadgets_produced}')
except ValueError:
    print('You entered an invalid number!')