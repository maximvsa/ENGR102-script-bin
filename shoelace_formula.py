# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   9.18 LAB: Shoelace formula
# Date:         18 October 2025

def getpoints(input_string):
    # Comment
    return [list(map(int, i.split(','))) for i in input_string.split()]

def cross(x, y):
    return x[0]*y[1] - x[1]*y[0]

def shoelace(z):
    total = 0
    n = len(z)
    # Summation series
    for i in range(n):
        total += cross(z[i], z[(i + 1) % n])
    return (1/2) * abs(total)

def main():
    input_string = input("Please enter the vertices: ")
    print(f"The area of the polygon is {shoelace(getpoints(input_string)):.1f}")

if __name__ == '__main__':
    main()