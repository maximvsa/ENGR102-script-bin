# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   7.17 LAB: Pig latin
# Date:         1 October 2025

raw_user_input = input("Enter word(s) to convert to Pig Latin: ")
word_list = raw_user_input.split()

# All English consonants:
consonant_list = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]

# All English vowels:
vowel_list = ["a", "e", "i", "o", "u", "y"]

# Special cases list (as per Zylabs):
special_cases = ["wh", "ch", "tr", "gr", "bl", "br", "th", "wr", "pr"]

neo_word_list = []

def word_thinger():
    for word in word_list:
        letter_list = list(word)
        if len(letter_list) < 2:
            if letter_list[0] in consonant_list:
                letter_list.append(letter_list[0] + "ay")
                letter_list.remove(letter_list[0])
            elif letter_list[0] in vowel_list:
                letter_list.append("yay")
            new_word = "".join(letter_list)
            neo_word_list.append(new_word)
            continue
        if letter_list[0] + letter_list[1] in special_cases:
            if letter_list[0] in consonant_list:
                letter_list.append(letter_list[0] + letter_list[1] + "ay")
                letter_list.remove(letter_list[0])
                letter_list.remove(letter_list[0])
            elif letter_list[0] in vowel_list:
                letter_list.append("yay")
            new_word = "".join(letter_list)
            neo_word_list.append(new_word)
            continue
        if letter_list[0] in consonant_list:
            letter_list.append(letter_list[0] + "ay")
            letter_list.remove(letter_list[0])
        elif letter_list[0] in vowel_list:
            letter_list.append("yay")
        new_word = "".join(letter_list)
        neo_word_list.append(new_word)

word_thinger()

pig_latin_sentence = " ".join(neo_word_list)

print(f'In Pig Latin, "{raw_user_input}" is: {pig_latin_sentence}')