# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Maximus Amick
#               Daniel Yoo
#               Caleb Carter
#               Noah Kim
# Section:      513
# Assignment:   Lab: Topic 12 (Team)
# Date:         11 November 2025

# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

import numpy as np
import matplotlib as plt

A = np.arange(12).reshape(3, 4)
B = np.arange(8).reshape(4, 2)
C = np.arange(6).reshape(2, 3)
D = A @ B @ C
E = np.sqrt(D) / 2

print(f"A = {A}")
print()
print(f"B = {B}")
print()
print(f"C = {C}")
print()
print(f"D = {D}")
print()
print(f"D^T = {np.transpose(D)}")
print()
print(f"E = {E}")