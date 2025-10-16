# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   8.17 LAB: ASCII clock
# Date:         16 October 2025

# Define list of characters that users are allowed to use for ASCII art
permitted_characters = list("abcdeghkmnopqrsuvwxyz@$&*=")

# Prompt user to enter time in HH:MM format
time = input("Enter the time: ")
# Split the time string into hours and minutes components
hours, _, minutes = time.partition(":")

# Loop until user enters a valid clock type (12 or 24)
while True:
    clock_type = input("Choose the clock type (12 or 24): ")
    if clock_type == "12" or clock_type == "24":
        break

# Handle midnight (00:00) in 12-hour format
if int(hours) == 0 and clock_type == "12":
    display_time = f"1 2 : {minutes[0]} {minutes[1]} A M"
# Handle single-digit AM hours (1-9) in 12-hour format
elif int(hours) < 10 and clock_type == "12":
    display_time = f"{hours} : {minutes[0]} {minutes[1]} A M"
# Handle double-digit AM hours (10-11) in 12-hour format
elif 12 > int(hours) >= 10 and clock_type == "12":
    display_time = f"{hours[0]} {hours[1]} : {minutes[0]} {minutes[1]} A M"
# Handle noon (12:00) in 12-hour format
elif int(hours) == 12 and clock_type == "12":
    display_time = f"1 2 : {minutes[0]} {minutes[1]} P M"
# Handle single-digit PM hours (13-21) in 12-hour format
elif 22 > int(hours) > 12 and clock_type == "12":
    display_time = f"{int(hours) - 12} : {minutes[0]} {minutes[1]} P M"
# Handle double-digit PM hours (22-23) in 12-hour format
elif int(hours) > 22 and clock_type == "12":
    display_time = f"{' '.join(str(int(hours) - 12))} : {minutes[0]} {minutes[1]} P M"
# Handle midnight (00:00) in 24-hour format
elif int(hours) == 0 and clock_type == "24":
    display_time = f"0 : {minutes[0]} {minutes[1]}"
# Handle single-digit hours (0-9) in 24-hour format
elif int(hours) < 10 and clock_type == "24":
    display_time = f"{hours} : {minutes[0]} {minutes[1]}"
# Handle double-digit hours (10-23) in 24-hour format
elif int(hours) >= 10 and clock_type == "24":
    display_time = f"{' '.join(hours)} : {minutes[0]} {minutes[1]}"

# Ask user for their preferred character to use in ASCII art
preferred_character = input("Enter your preferred character: ")
# Validate that the character is in the permitted list or is blank
while preferred_character not in permitted_characters:
    if preferred_character == "":
        break
    else:
        preferred_character = input("Character not permitted! Try again: ")

# Dictionary containing ASCII art patterns for each digit and character
ascii_art_dict = {
    " ": [' ', ' ', ' ', ' ', ' '],
    "0": ['***', '* *', '* *', '* *', '***'],
    "1": [' * ', '** ', ' * ', ' * ', '***'],
    "2": ['***', '  *', '***', '*  ', '***'],
    "3": ['***', '  *', '***', '  *', '***'],
    "4": ['* *', '* *', '***', '  *', '  *'],
    "5": ['***', '*  ', '***', '  *', '***'],
    "6": ['***', '*  ', '***', '* *', '***'],
    "7": ['***', '  *', '  *', '  *', '  *'],
    "8": ['***', '* *', '***', '* *', '***'],
    "9": ['***', '* *', '***', '  *', '***'],
    ":": [' ', ':', ' ', ':', ' '],
    "A": [' A ', 'A A', 'AAA', 'A A', 'A A'],
    "P": ['PPP', 'P P', 'PPP', 'P  ', 'P  '],
    "M": ['M   M', 'MM MM', 'M M M', 'M   M', 'M   M']}

# Replace default asterisks with user's preferred character
if preferred_character != "":
    for key_char in ascii_art_dict:
        # Iterate through each row of the ASCII art
        for row in range(len(ascii_art_dict[key_char])):
            ascii_art_dict[key_char][row] = ascii_art_dict[key_char][row].replace("*", preferred_character)
# If blank, replace asterisks with the actual character being displayed
elif preferred_character == "":
    for key_char in ascii_art_dict:
        # Iterate through each row of the ASCII art
        for row in range(len(ascii_art_dict[key_char])):
            ascii_art_dict[key_char][row] = ascii_art_dict[key_char][row].replace("*", key_char)
else:
    print("Something went wrong!")

# Print blank line for spacing
print()

# Print the ASCII clock by iterating through each row
for row in range(len(ascii_art_dict[key_char])):
    # Print each character of the display time horizontally
    for char in display_time:
        print(ascii_art_dict[char][row], end="")
    # Move to next line after completing a row
    print()
