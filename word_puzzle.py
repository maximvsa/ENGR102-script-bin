# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   9.19 LAB: Word puzzle
# Date:         18 October 2025

def print_puzzle(puzzle):
    ''' Print puzzle as a long division problem. '''
    puzzle = puzzle.split(',')
    for i in range(len(puzzle)):
        if i == 1:
            print(f'{len(puzzle[i].split("|")[1]) * "_": >16}')
        print(f'{puzzle[i]: >16}')
        if i > 1 and i % 2 == 0:
            print(f"{'-'*len(puzzle[i]): >16}")

def get_valid_letters(puzzle):
    valid_letters = []
    for i in list(puzzle):
        if i not in valid_letters and i.isalpha():
            valid_letters.append(i)
    return "".join(valid_letters)

def is_valid_guess(valid_letters_str, guess):
    if len(guess) != 10:
        return False
    if len(set(guess)) != len(guess):
        return False
    for i in list(guess):
        if i not in list(valid_letters_str):
            return False
    return True

def check_user_guess(dividend, quotient, divisor, remainder):
    if dividend == quotient * divisor + remainder:
        return True
    else:
        return False

def make_number(word, guess):
    digits = []
    for i in word:
        digits.append(str(guess.find(i)))
    return int("".join(digits))

def make_numbers(puzzle, guess):
    parts = [segment.strip() for segment in puzzle.split(",") if segment.strip()]
    quotient_word = parts[0]
    divisor_word = None
    dividend_word = None
    for segment in parts:
        if "|" in segment:
            left, right = segment.split("|", 1)
            divisor_word = left.strip()
            dividend_word = right.strip()
            break
    remainder_word = parts[-1]
    return make_number(dividend_word, guess), make_number(quotient_word, guess), make_number(divisor_word, guess), make_number(remainder_word, guess)

def main():
    # The lines below demonstrate what the print_puzzle function outputs.
    # Example puzzle: "RUE,EAR | RUMORS,UEII  ,UKTR ,EAR ,KEOS,KAIK,USA"
    puzzle = input("Enter a word arithmetic puzzle: ")
    print()
    print_puzzle(puzzle)
    print()
    guess = input("Enter your guess, for example ABCDEFGHIJ: ")
    if is_valid_guess(get_valid_letters(puzzle), guess) == False:
        print("Your guess should contain exactly 10 unique letters used in the puzzle.")
    else:
        dividend, quotient, divisor, remainder = make_numbers(puzzle, guess)
        if check_user_guess(dividend, quotient, divisor, remainder) == True:
            print("Good job!")
        else:
            print("Try again!")

if __name__ == '__main__':
    main()