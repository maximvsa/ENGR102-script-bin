# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   5.3 LAB: Diabetes risk
# Date:         18 September 2025

from math import *

# sex
sex = input('Enter your sex (M/F): ')

if sex.lower() == 'm':
    sex_risk_factor = 0
elif sex.lower() == 'f':
    sex_risk_factor = 0.879
else:
    print('Something went wrong!')

# age
age = int(input('Enter your age (years): '))

# bmi
bmi = float(input('Enter your BMI: '))

# range calculations for the possible domain of the user bmi input
# OMG I HATE WRITING COMMENTS THIS SUCKS
if bmi < 25:
    bmi_risk_factor = 0
elif 25 <= bmi < 27.5:
    bmi_risk_factor = 0.699
elif 27.5 <= bmi < 30:
    bmi_risk_factor = 1.97
elif bmi >= 30:
    bmi_risk_factor = 2.518
else:
    print('Something went wrong!')

# hypertension
hypertension_status = input('Are you on medication for hypertension (Y/N)? ')

if hypertension_status.lower() == 'y':
    hypertension_risk_factor = 1.222
elif hypertension_status.lower() == 'n':
    hypertension_risk_factor = 0
else:
    print('Something went wrong!')

# steroids
steroids_status = input('Are you on steroids (Y/N)? ')

if steroids_status.lower() == 'y':
    steroids_risk_factor = 2.191
elif steroids_status.lower() == 'n':
    steroids_risk_factor = 0
else:
    print('Something went wrong!')

# smoking
smoker_status = input('Do you smoke cigarettes (Y/N)? ')

if smoker_status.lower() == 'y':
    smoker_risk_factor = 0.855
elif smoker_status.lower() == 'n':
    past_smoker_status = input('Did you used to smoke (Y/N)? ')
    if past_smoker_status.lower() == 'y':
        smoker_risk_factor = -0.218
    elif past_smoker_status.lower() == 'n':
        smoker_risk_factor = 0
    else:
        print('Something went wrong!')
else:
    print('Something went wrong!')

# family history
family_history_status = input('Do you have a family history of diabetes (Y/N)? ')

if family_history_status.lower() == 'y':
    parents_and_sibling_status = input('Both parent and sibling (Y/N)? ')
    if parents_and_sibling_status.lower() == 'y':
        family_history_risk_factor = 0.753
    elif parents_and_sibling_status.lower() == 'n':
        family_history_risk_factor = 0.728
    else:
        print('Something went wrong!')
elif family_history_status.lower() == 'n':
    family_history_risk_factor = 0
else:
    print('Something went wrong!')

# n-formula: n = 6.322 + sex - (0.063 * age) - BMI - hypertension - steroids - smoker - history
# for risk = 100 / (1 + e^n)

n_variable = 6.322 + sex_risk_factor - (0.063 * age) - bmi_risk_factor - hypertension_risk_factor - steroids_risk_factor - smoker_risk_factor - family_history_risk_factor
risk = 100 / (1 + (e ** n_variable))

print(f'Your risk of developing type-2 diabetes is {risk:.1f}%')