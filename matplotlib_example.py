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

import numpy as np
import matplotlib.pyplot as plt

# // SECTION 1 //

x_values = np.linspace(-2, 2, num=10000)
y_func = lambda x, f: 0.25 * (1 / f) * np.pow(x, 2)

plt.figure(1)
plt.plot(x_values, y_func(x_values, 2), color="red", linewidth=2, label="f=2")
plt.plot(x_values, y_func(x_values, 6), color="blue", linewidth=6, label="f=6")
plt.legend()
plt.title("Parabola plots with varying focal length")
plt.xlabel("x")
plt.ylabel("y")

# // SECTION 2 //

x_values = np.linspace(-4, 4, num=25)
y_func = lambda x: 2*x**3 + 3*x**2 - 11*x - 6

plt.figure(2)
plt.scatter(x_values, y_func(x_values), color="yellow", marker="*", edgecolors="black", s=200)
plt.title("Plot of cubic polynomial")
plt.xlabel("x values")
plt.ylabel("y values")

# // SECTION 3 //

x_values = np.linspace(-2*np.pi, 2*np.pi, num=10000)
fig, axes = plt.subplots(nrows=2, ncols=1)
plt.suptitle("Plot of cos(x) and sin(x)")
plt.xlabel("x")

ax1 = axes[0]
ax2 = axes[1]

ax1.plot(x_values, np.cos(x_values), color="red", label="cos(x)")
ax1.legend(loc="lower right")
ax1.set_ylabel("y=cos(x)")
ax1.grid(True)

ax2.plot(x_values, np.sin(x_values), color="blue", label="sin(x)")
ax2.legend(loc="upper right")
ax2.set_ylabel("y=sin(x)")
ax2.grid(True)

# SHOW DAT STUFF
plt.show()