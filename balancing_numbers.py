# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   6.21 LAB: Balancing numbers
# Date:         23 September 2025

import math

n_input = int(input('Enter a value for n: '))


first_sum = 0
second_sum = 0
potential_balancer = 0

# one-line check for a balancing number
if math.isqrt(1 + 8*n_input*n_input)**2 == 1 + 8*n_input*n_input and (math.isqrt(1 + 8*n_input*n_input) - 1) % 2 == 0 and (math.isqrt(1 + 8*n_input*n_input) - 1)//2 > n_input:
    for i in range(1, n_input):            # sum 1..(n-1)
        first_sum += i
    while True:
        potential_balancer += 1
        second_sum = 0
        for i in range(n_input + 1, n_input + potential_balancer + 1):
            second_sum += i

# BALANCER SPOTTED!!!
        if second_sum == first_sum:
            break
    print(f'{n_input} is a balancing number with r={potential_balancer}')
else:
    print(f'{n_input} is not a balancing number')