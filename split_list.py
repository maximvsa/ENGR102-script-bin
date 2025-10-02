# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   7.19 LAB: Split list
# Date:         2 October 2025

full_numbers_list = input("Enter numbers: ").split()
full_numbers_list = [int(i) for i in full_numbers_list]

# The space immediately after the index given by split_spot is the point where the list chops in two to sum
# If split_spot = 1, the space after index of 1 is the point where the list is "split"
split_spot = 0
is_valid_split = False

def main():
    global split_spot
    global is_valid_split
    for index in full_numbers_list[:]:
        left_sum = 0
        right_sum = 0
        for number in full_numbers_list[:split_spot+1]:
            left_sum += number
        for number in full_numbers_list[split_spot+1:]:
            right_sum += number
        if left_sum == right_sum:
            print(f"Left: {full_numbers_list[:split_spot+1]}")
            print(f"Right: {full_numbers_list[split_spot+1:]}")
            print(f"Both sum to {left_sum}")
            is_valid_split = True
            break
        split_spot += 1
    if is_valid_split == False:
        print("Cannot split evenly")

if __name__ == "__main__":
    main()