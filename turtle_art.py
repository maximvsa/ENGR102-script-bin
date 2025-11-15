# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   Lab: Topic 13 (individual)
# Date:         20 November 2025

import turtle as t

def parta(angle):
    t.dot(10, "red")
    iterations = 0
    initial_angle = angle
    while angle != 0:
        angle = (angle + initial_angle) % 360
        t.setheading(angle)
        t.forward(100)
        iterations += 1
    angle = (angle + initial_angle) % 360
    t.setheading(angle)
    t.forward(50)
    iterations += 1
    t.done()
    return iterations

def partb(sequence):
    from math import pi, sin, cos
    angle = 0
    x_position = 0
    y_position = 0
    for char in list(sequence):
        if char == 0:
            angle = (angle + 30) % 360
            x_position += cos(angle*pi/180)
            y_position += sin(angle*pi/180)
        elif char == 1:
            angle = (angle - 141) % 360
    while angle != 0 and x_position != 0 and y_position != 0:
        pass

def main():
    print(parta(141))

if __name__ == "__main__":
    main()