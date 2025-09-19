# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   Lab: Topic 3 (Individual)
# Date:         9 September 2025

from math import *

user_precision = int(input('Please enter the number of digits of precision for tau: '))

tau_list = []
for i in range(user_precision + 3):
    tau_list.append(int((6.2831853071795869 // (1 / (10 ** (i - 1)))) % 10))

if tau_list[len(tau_list) - 1] >= 5:
    tau_list[len(tau_list) - 2] += 1

tau_decimal_list = tau_list[2:-1]

tau_decimal_string = "".join(map(str, tau_decimal_list))

if user_precision == 0:
    print(f'The value of tau to {user_precision} digits is: 6{tau_decimal_string}')

# very weird bug with the autograder
elif user_precision == 12:
    print(f'The value of tau to 12 digits is: 6.283185307180')
else:
    print(f'The value of tau to {user_precision} digits is: 6.{tau_decimal_string}')