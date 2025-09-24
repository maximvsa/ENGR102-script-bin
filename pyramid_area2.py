# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   6.12 LAB: Pyramid area (part 2)
# Date:         23 September 2025

side_length = float(input("Enter the side length in meters: "))
number_of_layers = int(input("Enter the number of layers: "))

uncovered_panel_area = side_length ** 2

# Calculate the total area of the pyramid from the top-down view
top_area = uncovered_panel_area * (number_of_layers ** 2)

# Calculate the area of one side panel
one_side_area = uncovered_panel_area * (number_of_layers * (number_of_layers + 1) / 2)

total_area = top_area + 4 * one_side_area

# Output the total area needed to cover the pyramid
print(f"You need {total_area:.2f} m^2 of gold foil to cover the pyramid")