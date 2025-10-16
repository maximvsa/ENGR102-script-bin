import numpy as np

x_span = np.linspace(0, 6, num=1000)
y_span = np.linspace(0, np.pi/4, num=1000)

dx = x_span[1] - x_span[0]
dy = y_span[1] - y_span[0]

double_integral = 0

f = lambda x, y: x * (np.cos(y)**-2)

for n1 in y_span:
    integral = 0
    for n2 in x_span:
        integral += f(n2, n1) * dx
    double_integral += integral * dy

print(double_integral)