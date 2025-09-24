# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   6.17 LAB: Computing sums
# Date:         23 September 2025

integer_1 = int(input('Enter an integer: '))
integer_2 = int(input('Enter another integer: '))

# sum will only start at zero, to be increased within the for loop
sum = 0

for i in range(integer_1, integer_2 + 1):
    sum += i

print(f'The sum of all integers from {integer_1} to {integer_2} is {sum}')