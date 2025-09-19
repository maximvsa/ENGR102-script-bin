# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   Lab: Topic 3 (Individual)
# Date:         9 September 2025

import math

def reynolds_number_calculator(fluid_velocity, characteristic_linear_dimension, kinematic_viscocity):
    reynolds_number = (fluid_velocity * characteristic_linear_dimension) / kinematic_viscocity
    return reynolds_number

def braggs_law_wavelength_calculator(atomic_plane_distance, scatter_angle_degrees, diffraction_order):
    scatter_angle_radians = scatter_angle_degrees * (math.pi / 180)
    braggs_law_wavelength = (2 * atomic_plane_distance * math.sin(scatter_angle_radians)) / diffraction_order
    return braggs_law_wavelength

def arps_equation_production_rate_calculator(initial_production_rate, initial_decline_rate, hyperbolic_constant, time):
    arps_equation_production_rate = initial_production_rate / ((1 + hyperbolic_constant * initial_decline_rate * time) ** (1 / hyperbolic_constant))
    return arps_equation_production_rate

def tsiolkovsky_rocket_equation_change_of_velocity_calculator(exhaust_velocity, initial_mass, final_mass):
    tsiolkovsky_rocket_equation_change_of_velocity = exhaust_velocity * math.log(initial_mass / final_mass)
    return tsiolkovsky_rocket_equation_change_of_velocity

# I feel like I don't need to comment on this script, because it reads like English

print('This program calculates the Reynolds number given velocity, length, and viscosity')
user_fluid_velocity = float(input('Please enter the velocity (m/s): '))
user_length = float(input('Please enter the length (m): '))
user_viscocity = float(input('Please enter the viscosity (m^2/s): '))
print(f'Reynolds number is {reynolds_number_calculator(user_fluid_velocity, user_length, user_viscocity):.0f}')
print()

print('This program calculates the wavelength given distance and angle')
user_distance = float(input('Please enter the distance (nm): '))
user_angle = float(input('Please enter the angle (degrees): '))
print(f'Wavelength is {braggs_law_wavelength_calculator(user_distance, user_angle, 1):.4f} nm')
print()

print('This program calculates the production rate given time, initial rate, and decline rate')
user_time = float(input('Please enter the time (days): '))
user_initial_rate = float(input('Please enter the initial rate (barrels/day): '))
user_decline_rate = float(input('Please enter the decline rate (1/day): '))
print(f'Production rate is {arps_equation_production_rate_calculator(user_initial_rate, user_decline_rate, 0.8, user_time):.2f} barrels/day')
print()

print('This program calculates the change of velocity given initial mass, final mass, and exhaust velocity')
user_initial_mass = float(input('Please enter the initial mass (kg): '))
user_final_mass = float(input('Please enter the final mass (kg): '))
user_exhaust_velocity = float(input('Please enter the exhaust velocity (m/s): '))
print(f'Change of velocity is {tsiolkovsky_rocket_equation_change_of_velocity_calculator(user_exhaust_velocity, user_initial_mass, user_final_mass):.1f} m/s')