# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   Lab: Topic 12 (individual)
# Date:         12 November 2025

# // IMPORTS //

import numpy as np
import matplotlib.pyplot as plt

# // CONFIGURATION //

x = 0
y = 1
a = 1.02
b = 0.095
c = -0.095
d = 1.02

# // LE PROGRAMME //

v = np.array([x, y]).reshape(2, 1)
M = np.array([a, b, c, d]).reshape(2, 2)
point_bank = [v]

for i in range(250):
    if i == 0:
        v_prime = (M @ v).reshape(2, 1)
    else:
        v_prime = (M @ v_prime).reshape(2, 1)
    point_bank.append(v_prime)

# PLOT IT UP

plt.figure(1)
for i in range(250):
    plt.scatter(point_bank[i][0], point_bank[i][1])
plt.title("Logarithmic Spiral")
plt.xlabel("x")
plt.ylabel("y")
plt.show()