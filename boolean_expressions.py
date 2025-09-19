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

############ Part A ############

a = input("Enter True or False for a: ")
b = input("Enter True or False for b: ")
c = input("Enter True or False for c: ")

match a:
    case 't' | 'T' | 'true' | 'True' | 'TRUE' | '1' | 'y' | 'Y' | 'yes' | 'Yes' | 'YES':
        a = True
    case 'f' | 'F' | 'false' | 'False' | 'FALSE' | '0' | 'n' | 'N' | 'no' | 'No' | 'NO':
        a = False

match b:
    case 't' | 'T' | 'true' | 'True' | 'TRUE' | '1' | 'y' | 'Y' | 'yes' | 'Yes' | 'YES':
        b = True
    case 'f' | 'F' | 'false' | 'False' | 'FALSE' | '0' | 'n' | 'N' | 'no' | 'No' | 'NO':
        b = False

match c:
    case 't' | 'T' | 'true' | 'True' | 'TRUE' | '1' | 'y' | 'Y' | 'yes' | 'Yes' | 'YES':
        c = True
    case 'f' | 'F' | 'false' | 'False' | 'FALSE' | '0' | 'n' | 'N' | 'no' | 'No' | 'NO':
        c = False

############ Part B ############ 

# AND
match (a, b, c):
    case (True, True, True):
        print("a and b and c: True")
    case _:
        print("a and b and c: False")

# OR
match (a, b, c):
    case (False, False, False):
        print("a or b or c: False")
    case _:
        print("a or b or c: True")

############ Part C ############ 

# XOR
match (a, b):
    case (True, True) | (False, False):
        print("XOR: False")
    case _:
        print("XOR: True")

match (a, b, c):
    case (True, True, True) | (True, False, False) | (False, True, False) | (False, False, True):
        print('Odd number: True')
    case _:
        print('Odd number: False')

############ Part D ############

complex_expression_1 = (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
simple_expression_1 = not b and not a or not a and b and not c or a and not b

complex_expression_2 = (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))
simple_expression_2 = not b and c or a and c or a and b and not c or a and not b and not c

print(f'Complex 1: {complex_expression_1}')
print(f'Complex 2: {complex_expression_2}')
print(f'Simple 1: {simple_expression_1}')
print(f'Simple 2: {simple_expression_2}')
