# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   6.19 LAB: Juggler sequence
# Date:         23 September 2025

import math

i = int(input('Enter a positive integer: '))
iteration_counter = 0

if i == 1:
    print('The Juggler sequence starting at 1 is:')
    print('1')
    print('It took 0 iterations to reach 1')

else:
    print(f'The Juggler sequence starting at {i} is:')
    print(f'{i}, ', end = '')

    while True:

    # sequence termination
        if i == 2:
            print(f'1\nIt took {iteration_counter + 1} iterations to reach 1')
            break

    # if its even
        elif i % 2 == 0:
            i = math.floor(math.sqrt(i))
            print(f'{i:.0f}, ', end = '')

    # if its odd / catch all
        else:
            i = math.floor(i ** (3/2))
            print(f'{i:.0f}, ', end = '')
        iteration_counter += 1