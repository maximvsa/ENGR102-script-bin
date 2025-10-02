# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   7.18 LAB: The Name Game
# Date:         1 October 2025

name = input("What is your name? ")

# All English consonants:
consonant_list = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]

# All English vowels:
vowel_list = ["a", "e", "i", "o", "u", "y"]

# Special cases list (as per Zylabs):
special_cases = ["wh", "ch", "tr", "gr", "bl", "br", "th", "wr", "pr"]

# Takes every letter of the name after the first one
# Okay nevermind then
if name[0].lower() + name[1] in special_cases:
    if name[0].lower() in vowel_list:
        shortened_name = name[2:]
    elif name[0].lower() in consonant_list and name[2] in consonant_list:
        shortened_name = name[3:]
    else:
        shortened_name = name[2:]
else:
    if name[0].lower() in vowel_list:
        shortened_name = name.lower()
    elif name[0].lower() in consonant_list and name[1] in consonant_list:
        shortened_name = name[2:]
    else:
        shortened_name = name[1:]

print(f"{name}, {name}, Bo-B{shortened_name}")
print(f"Banana-Fana Fo-F{shortened_name}")
print(f"Me Mi Mo-M{shortened_name}")
print(name, end="!")