# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   4.22 LAB: Tank volume
# Date:         13 September 2025

from math import *

tank_height = float(input('Enter the tank height: '))
liquid_height = float(input('Enter the liquid height: '))
tank_radius = float(input('Enter the tank radius: '))

# equations for spheres and circular cylinders
if liquid_height < tank_radius:
    tank_volume = (pi / 3) * (liquid_height ** 2) * ((3 * tank_radius) - liquid_height)
elif tank_radius <= liquid_height < (tank_height - tank_radius):
    tank_volume = (4 / 6) * pi * (tank_radius ** 3) + pi * (tank_radius ** 2) * (liquid_height - tank_radius)
elif liquid_height > (tank_height - tank_radius):
    full_tank_volume = (4 / 3) * pi * (tank_radius ** 3) + pi * (tank_radius **2) * (tank_height - (2 * tank_radius))
    tank_volume = full_tank_volume - ((pi / 3) * ((tank_height - liquid_height) ** 2) * ((3 * tank_radius) - (tank_height - liquid_height)))

try:
    print(f'The volume of the liquid is {tank_volume:.3f}')
except NameError:
    print('an error occured')