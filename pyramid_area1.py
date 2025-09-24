# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   6.11 LAB: Pyramid area (part 1)
# Date:         23 September 2025

side_length = float(input("Enter the side length in meters: "))
number_of_layers = int(input("Enter the number of layers: "))

uncovered_panel_area = side_length ** 2
total_area = 0

# Calculate the area of each layer's top and side area and add it to the total area
for layer in range(1, number_of_layers + 1):
    layer_top_area = uncovered_panel_area * (layer ** 2) - uncovered_panel_area * ((layer - 1) ** 2)
    total_area += layer_top_area

    layer_side_area = 4 * side_length ** 2 * layer
    total_area += layer_side_area

# Output the total area needed to cover the pyramid
print(f"You need {total_area:.2f} m^2 of gold foil to cover the pyramid")
