# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   7.20 LAB: Kaprekar's constant
# Date:         2 October 2025

def main():
    user_input = input("Enter a four-digit integer: ")
    number = int(user_input)
    
    # Handle special case where input is already 6174
    if number == 6174:
        print(f"{user_input} reaches 6174 via Kaprekar's routine in 0 iterations")
        return
    
    iterations = 0
    history = [number]
    
    while number != 6174:
        # Get the 4 digits
        digit1 = (number // 1000) % 10
        digit2 = (number // 100) % 10
        digit3 = (number // 10) % 10
        digit4 = number % 10
        
        # Find largest number by sorting digits high to low
        digits = [digit1, digit2, digit3, digit4]
        larger_number = 0
        for i in range(4):
            max_digit = max(digits)
            larger_number = larger_number * 10 + max_digit
            digits.remove(max_digit)
        
        # Find smallest number by sorting digits low to high
        digits = [digit1, digit2, digit3, digit4]
        smaller_number = 0
        for i in range(4):
            min_digit = min(digits)
            smaller_number = smaller_number * 10 + min_digit
            digits.remove(min_digit)
        
        # Subtract and continue
        number = larger_number - smaller_number
        
        # If we get 0, all digits were the same - can't reach 6174
        if number == 0:
            print(f"{user_input} > 0")
            print(f"{user_input} reaches 0 via Kaprekar's routine in 1 iterations")
            return
        
        history.append(number)
        iterations += 1
    
    # Print the history
    history_string = ""
    for i in range(len(history)):
        if i == 0:
            history_string += str(history[i])
        else:
            history_string += " > " + str(history[i])
    
    print(history_string)
    print(f"{user_input} reaches 6174 via Kaprekar's routine in {iterations} iterations")

if __name__ == "__main__":
    main()