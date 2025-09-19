# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   Lab: Topic 1
# Date:         29 August 2025

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

print(f'Reynolds number is {reynolds_number_calculator(9, 0.875, 0.0015)}')
print(f'Wavelength is {braggs_law_wavelength_calculator(0.029, 35, 1)} nm')
print(f'Production rate is {arps_equation_production_rate_calculator(100, 2, 0.8, 10)} barrels/day')
print(f'Change of velocity is {tsiolkovsky_rocket_equation_change_of_velocity_calculator(2029, 11000, 8300)} m/s')