# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   6.20 LAB: Co-balancing numbers
# Date:         23 September 2025

import math

n_input = int(input('Enter a value for n: '))


first_sum = 0
second_sum = 0
potential_co_balancer = 0

# very long line that checks if the input is a co-balancing number or not
if math.isqrt(1 + 8*n_input*(n_input+1))**2 == 1 + 8*n_input*(n_input+1) and (math.isqrt(1 + 8*n_input*(n_input+1)) - 1) % 2 == 0 and (math.isqrt(1 + 8*n_input*(n_input+1)) - 1)//2 > n_input:
    for i in range(1, n_input + 1):
        first_sum += i
    while True:
        potential_co_balancer += 1
        second_sum = 0
        for i in range(n_input + 1, n_input + potential_co_balancer + 1):
            second_sum += i

# COBALANCER SPOTTED!!!
        if second_sum == first_sum:
            break
    print(f'{n_input} is a co-balancing number with r={potential_co_balancer}')
else:
    print(f'{n_input} is not a co-balancing number')