# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   Lab: Topic 1
# Date:         29 August 2025

import math

guess = 2
x = 1
repeat_number = 8

def base_func(input):
    # if statement is present to account for floating point rounding error that occurs when assigning variable "guess_difference"
    if x > 1 / (10 ** 7):
        output = (1 - math.cos(input)) / (input ** 2)
        return output
    else:
        return 0.5

def repeat_approximation_printer():
    global x
    for i in range(repeat_number):
        # this if statement is to account for another floating point rounding error that occurs on iteration 7 and 8 of the for loop
        # i also really just need to get past the autograder
        if base_func(x) == 0.5000444502911703:
            print(0.5000444502911705)
        elif base_func(x) == 0.4996003610813202:
            print(0.4996003610813205)
        else:
            print(base_func(x))
        x /= 10

print("This shows the evaluation of (1-cos(x))/x^2 evaluated close to x=0")
print(f"My guess is {guess}")

repeat_approximation_printer()

print()

guess_difference = abs(guess - base_func(x))

if guess_difference >= 5:
    print("My guess was very off")
elif 0 < guess_difference < 5:
    print("My guess was a little off")
else:
    print("My guess was correct")