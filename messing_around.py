import numpy as np
import matplotlib.pyplot as plt

u = np.linspace(0, 2, 1000)
v = np.linspace(0, 2, 1000)
w = np.linspace(0, 2, 1000)
u_mesh, v_mesh, w_mesh = np.meshgrid(u, v, w)

x_mesh = u_mesh * (v_mesh ** 4) + (w_mesh ** 3)
y_mesh = u_mesh + v_mesh * np.exp(w_mesh)

z_mesh = (x_mesh ** 4) + x_mesh * (y_mesh ** 3)
print(z_mesh)