# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   8.19 LAB: Count words
# Date:         16 October 2025

targeted_word_count_dict = {}
unique_words = {}

sentence = input("Enter a sentence: ").replace(',', '').replace('!', '').replace('.', '').replace('?', '').lower().split()

words_to_count = input("Enter some words: ").lower().split()

for word in sentence:
    if word not in unique_words:
        unique_words[word] = 1
    else:
        unique_words[word] += 1

for word in words_to_count:
    if word in sentence and word not in targeted_word_count_dict:
        targeted_word_count_dict[word] = unique_words[word]
    elif word not in sentence:
        targeted_word_count_dict[word] = 0

for word in targeted_word_count_dict:
    if targeted_word_count_dict[word] == 0:
        print(f'The word "{word}" does not appear in the sentence')
    elif targeted_word_count_dict[word] == 1:
        print(f'The word "{word}" appears 1 times in the sentence')
    elif targeted_word_count_dict[word] >= 2:
        print(f'The word "{word}" appears {unique_words[word]} times in the sentence')

# Comment
if len(unique_words) == 1:
    print("There are 1 unique words in the sentence")
elif len(unique_words) >= 2:
    print(f"There are {len(unique_words)} unique words in the sentence")
