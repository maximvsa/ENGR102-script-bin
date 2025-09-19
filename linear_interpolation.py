# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Maximus Amick
#               Jace Flanagan
#               Matthew Rapacki
#               Corbin Shaw
# Section:      513
# Assignment:   Lab: Topic 2 (Team)
# Date:         2 September 2025

import math

time = 25

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

    # y = (slope)(x - x1) + y1
    # the above equation cannot be implemented in the linear interpolator function as-is because, even if "slope," "x," "x1," and "y1" were variables locally defined within the function, 
    # it would evaluate "x - x1" as a float and then attempt to call that float due to "x - x1" being enclosed in parenthesis, resulting in a type error
    # the point slope equation is used to define the interpolated coordinates within the linear interpolator function, it just uses more readable variables for the sake of clarity and code adaptability

    return interpolated_x, interpolated_y, interpolated_z

def printer():
    global time
    print("Part 1:")
    print(f'For t = {time} minutes, the position p = {linear_interpolator(point1, point2)[0]} kilometers')
    time = 300
    print("Part 2:")
    print(f'For t = {time} minutes, the position p = {linear_interpolator(point1, point2)[0] % (2 * math.pi * 6745)} kilometers')

if __name__ == '__main__':
    point1 = Point(2029, 0, 0, 10)
    point2 = Point(23029, 0, 0, 55)

    printer()