# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   Lab: Topic 2 (Individual)
# Date:         2 September 2025

import math

time = 30
print_iterations = 5

class Point:
    def __init__(self, x, y, z, t):
        self.x = x
        self.y = y
        self.z = z
        self.t = t
    
def linear_interpolator(initial_point, terminal_point):
    dx = terminal_point.x - initial_point.x
    dy = terminal_point.y - initial_point.y
    dz = terminal_point.z - initial_point.z
    dt = terminal_point.t - initial_point.t
    interpolated_x = ((dx / dt) * (time - initial_point.t)) + initial_point.x
    interpolated_y = ((dy / dt) * (time - initial_point.t)) + initial_point.y
    interpolated_z = ((dz / dt) * (time - initial_point.t)) + initial_point.z
    return interpolated_x, interpolated_y, interpolated_z

def printer():
    global time, print_iterations
    for i in range(print_iterations):
        print(f'At time {time:.1f} seconds:')
        print(f'x{i + 1} = {linear_interpolator(point1, point2)[0]} m')
        print(f'y{i + 1} = {linear_interpolator(point1, point2)[1]} m')
        print(f'z{i + 1} = {linear_interpolator(point1, point2)[2]} m')
        if print_iterations > 1:
            print("-----------------------")
        time += 7.5
        print_iterations -= 1

# comment, comment, comment

if __name__ == '__main__':
    point1 = Point(8, 6, 7, 12)
    point2 = Point(-5, 30, 9, 85)

    printer()