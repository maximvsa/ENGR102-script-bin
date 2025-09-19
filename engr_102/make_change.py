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

payment = float(input('How much did you pay? '))
cost = float(input('How much did it cost? '))

print(f'You received ${payment - cost:.2f} in change. That is...')

change = payment - cost
cent_change = change * 100

# quarter = 25 cents
# dime = 10 cents
# nickel = 5 cents
# pennie = 1 cent

change_quarters = cent_change // 25
cent_change = cent_change - (25 * change_quarters)

change_dimes = cent_change // 10
cent_change = cent_change - (10 * change_dimes)

change_nickels = cent_change // 5
cent_change = cent_change - (5 * change_nickels)

change_pennies = cent_change
change_pennies = round(change_pennies, 1)

if 0 < change_quarters <= 1:
    print(f'{change_quarters:.0f} quarter')
elif change_quarters > 1:
    print(f'{change_quarters:.0f} quarters')

if 0 < change_dimes <= 1:
    print(f'{change_dimes:.0f} dime')
elif change_dimes > 1:
    print(f'{change_dimes:.0f} dimes')



if 0 < change_nickels <= 1:
    print(f'{change_nickels:.0f} nickel')
elif change_nickels > 1:
    print(f'{change_nickels:.0f} nickels')

if 0 < change_pennies <= 1:
    print(f'{change_pennies:.0f} penny')
elif change_pennies > 1:
    print(f'{change_pennies:.0f} pennies')