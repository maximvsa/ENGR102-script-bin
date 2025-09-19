# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   4.14 LAB: Triangle math
# Date:         13 September 2025

hypotenuse = float(input('Enter the hypotenuse: '))
opposite_side = float(input('Enter the opposite side: '))
adjacent_side = float(input('Enter the adjacent side: '))

# pythagorean theorem guard
if ((adjacent_side ** 2) + (opposite_side ** 2) == (hypotenuse **2)):

    print('What would you like to calculate?')
    user_trig_operation_input = int(input('1: sin(θ), 2: cos(θ), 3: tan(θ), 4: csc(θ), 5: sec(θ), 6: cot(θ): '))

    match user_trig_operation_input:
        case 1:
            print(f'For a right triangle of sides {opposite_side}, {adjacent_side}, and {hypotenuse}, sin(θ) = {opposite_side / hypotenuse:.1f}')
        case 2:
            print(f'For a right triangle of sides {opposite_side}, {adjacent_side}, and {hypotenuse}, cos(θ) = {adjacent_side / hypotenuse:.1f}')
        case 3:
            print(f'For a right triangle of sides {opposite_side}, {adjacent_side}, and {hypotenuse}, tan(θ) = {opposite_side / adjacent_side:.1f}')
        case 4:
            print(f'For a right triangle of sides {opposite_side}, {adjacent_side}, and {hypotenuse}, csc(θ) = {1 / (opposite_side / hypotenuse):.1f}')
        case 5:
            print(f'For a right triangle of sides {opposite_side}, {adjacent_side}, and {hypotenuse}, sec(θ) = {1 / (adjacent_side / hypotenuse):.1f}')
        case 6:
            print(f'For a right triangle of sides {opposite_side}, {adjacent_side}, and {hypotenuse}, cot(θ) = {1 / (opposite_side / adjacent_side):.1f}')
        case _:
            exit(1)
else:
    print("Those lengths don't form a right triangle!")