# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   6.18 LAB: Collatz conjecture
# Date:         23 September 2025

i = int(input('Enter an integer: '))
iteration_counter = 0

if i == 1:
    print('Here is the Collatz sequence starting at 1:')
    print('1')
    print('It took 0 iterations to reach 1')

else:
    print(f'Here is the Collatz sequence starting at {i}:')
    print(f'{i}, ', end = '')

    while True:

    # sequence termination
        if i == 2:
            print(f'1\nIt took {iteration_counter + 1} iterations to reach 1')
            break

    # if its even
        elif i % 2 == 0:
            i /= 2
            print(f'{i:.0f}, ', end = '')

    # if its odd / catch all
        else:
            i = 3 * i + 1
            print(f'{i:.0f}, ', end = '')
        iteration_counter += 1