# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   6.16 LAB: Howdy Whoop
# Date:         23 September 2025

integer_1 = int(input('Enter an integer: '))
integer_2 = int(input('Enter another integer: '))

for i in range(1, 101):
    if i % integer_1 != 0 and i % integer_2 != 0:
        print(i)
    elif i % integer_1 == 0 and i % integer_2 != 0:
        print('Howdy')
    elif i % integer_1 != 0 and i % integer_2 == 0:
        print('Whoop')
    elif i % integer_1 == 0 and i % integer_2 == 0:
        print('Howdy Whoop')

    # error catcher to see if anything unexpected happens
    else:
        print('error')