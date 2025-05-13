import numpy as np
import matplotlib.pyplot as plt

# Boshlang‘ich shartlar
x0 = 0.7
y0 = 0.5
z0 = 0  # Taxminiy y'(0.7)
h = 0.1
x_end = 1.0

# Qadamlar soni
n_steps = int((x_end - x0) / h)

# x, y va z uchun massivlar
x_values = np.linspace(x0, x_end, n_steps + 1)
y_values = np.zeros(n_steps + 1)
z_values = np.zeros(n_steps + 1)
y_values[0] = y0
z_values[0] = z0

# Differentsial tenglama tizimi
def f1(x, y, z):
    return z

def f2(x, y, z):
    return x - (1/x) * z - 2 * y

# Runge-Kutta metodi
for i in range(n_steps):
    x_n = x_values[i]
    y_n = y_values[i]
    z_n = z_values[i]

    k1 = f1(x_n, y_n, z_n)
    l1 = f2(x_n, y_n, z_n)

    k2 = f1(x_n + h/2, y_n + (h/2) * k1, z_n + (h/2) * l1)
    l2 = f2(x_n + h/2, y_n + (h/2) * k1, z_n + (h/2) * l1)

    k3 = f1(x_n + h/2, y_n + (h/2) * k2, z_n + (h/2) * l2)
    l3 = f2(x_n + h/2, y_n + (h/2) * k2, z_n + (h/2) * l2)

    k4 = f1(x_n + h, y_n + h * k3, z_n + h * l3)
    l4 = f2(x_n + h, y_n + h * k3, z_n + h * l3)

    y_values[i + 1] = y_n + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
    z_values[i + 1] = z_n + (h/6) * (l1 + 2*l2 + 2*l3 + l4)

# Natijalarni chiqarish
print("Runge-Kutta metodi natijalari:")
for x, y, z in zip(x_values, y_values, z_values):
    print(f"x = {x:.1f}, y = {y:.4f}, y' = {z:.4f}")

# Grafik chizish
plt.plot(x_values, y_values, 'o-', label='y(x)', color='blue')
plt.plot(x_values, z_values, 'o-', label="y'(x)", color='red')
plt.xlabel('x')
plt.ylabel('y va y\'')
plt.title('Runge-Kutta metodi yordamida y(x) va y\'(x) (1-savol)')
plt.grid(True)
plt.legend()
plt.show()