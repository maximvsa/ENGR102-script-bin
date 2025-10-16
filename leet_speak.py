# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   8.18 LAB: Leet speak
# Date:         16 October 2025

leet_dict = {"a": "4", "e": "3", "o": "0", "s": "5", "t": "7"}

text = input("Enter some text: ")
leet_text = []
# compile each character into a list containing the leeted version of each character
for char in text:
    if char in leet_dict:
        leet_text.append(leet_dict[char])
    else:
        leet_text.append(char)

print(f'In leet speak, "{text}" is: \n{"".join(leet_text)}')