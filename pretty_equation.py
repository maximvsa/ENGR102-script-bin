# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Maximus Amick
#               Daniel Yoo
#               Caleb Carter
#               Noah Kim
# Section:      513
# Assignment:   Lab: Topic 4 (Team)
# Date:         17 September 2025

coeff_a = int(input("Please enter the coefficient A: "))
coeff_b = int(input("Please enter the coefficient B: "))
coeff_c = int(input("Please enter the coefficient C: "))


# equation: a * (x ** 2) + b * x + c

a = (f"{coeff_a}x^2")
b = (f"{coeff_b}x")
c = coeff_c

# CHECKPOINT 1

if (abs(coeff_a) == 1) or (abs(coeff_b)) == 1 or (abs(coeff_c == 1)):
    if (coeff_a == 1):
        a = " x^2"
    elif (coeff_a == -1):
        a = " - x^2"
    if (coeff_b == 1):
        b = " + x"
    elif (coeff_b == -1):
        b = " - x"
    if (coeff_c == 1):
        c = " + 1"
    elif (coeff_c == -1):
        c = " - 1"

# CHECKPOINT 2

if (coeff_a == 0 or coeff_b == 0 or coeff_c == 0):
    if (coeff_a == 0):
        a = ""
    if (coeff_b == 0):
        b = ""
    if (coeff_c == 0):
        c = ""

# CHECKPOINT 3

if coeff_a < -1:
    if (coeff_a < 0):
        a = (f" - {abs(coeff_a)}x^2")

if coeff_b < -1:
    if (coeff_b < 0):
        b = (f" - {abs(coeff_b)}x")

if coeff_c < -1:
    if (coeff_c < 0):
        c = (f" - {abs(coeff_c)}")

# CHECKPOINT 4

if (coeff_a > 1 or coeff_b > 1 or coeff_c > 1):
    if(coeff_a > 1):
        a = (f" {coeff_a}x^2")
    if(coeff_b > 1):
        if a != '':
            b = (f" + {coeff_b}x")
        else:
            b = (f' {coeff_b}x')
    if(coeff_c > 1):
        c = (f" + {coeff_c}")

if coeff_a == 0 and coeff_b == 1:
    b = f' x'

# CHECKPOINT 5

print(f'The quadratic equation is{a}{b}{c} = 0')