# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Maximus Amick
#               Daniel Yoo
#               Caleb Carter
#               Noah Kim
# Section:      513
# Assignment:   Lab: Topic 3 (Team)
# Date:         8 September 2025

import math

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
    interpolated_x = ((dx / dt) * (base_time - initial_point.t)) + initial_point.x
    interpolated_y = ((dy / dt) * (base_time - initial_point.t)) + initial_point.y
    interpolated_z = ((dz / dt) * (base_time - initial_point.t)) + initial_point.z
    return interpolated_x, interpolated_y, interpolated_z

def printer():
    global base_time, print_iterations, user_point_1_t, user_point_2_t
    for i in range(print_iterations):
        print(f'At time {base_time:.2f} seconds the object is at ({linear_interpolator(point1, point2)[0]:.3f}, {linear_interpolator(point1, point2)[1]:.3f}, {linear_interpolator(point1, point2)[2]:.3f})')

        base_time += (user_point_2_t - user_point_1_t) / 4
        print_iterations -= 1

# comment, comment, comment

user_point_1_t = float(input("Enter time 1: "))
user_point_1_x = float(input(f'Enter the x position of the object at time 1: '))
user_point_1_y = float(input(f'Enter the y position of the object at time 1: '))
user_point_1_z = float(input(f'Enter the z position of the object at time 1: '))

base_time = user_point_1_t

user_point_2_t = float(input("Enter time 2: "))
user_point_2_x = float(input(f'Enter the x position of the object at time 2: '))
user_point_2_y = float(input(f'Enter the y position of the object at time 2: '))
user_point_2_z = float(input(f'Enter the z position of the object at time 2: '))

print()

point1 = Point(user_point_1_x, user_point_1_y, user_point_1_z, user_point_1_t)
point2 = Point(user_point_2_x, user_point_2_y, user_point_2_z, user_point_2_t)
printer()