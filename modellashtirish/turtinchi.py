#  7.1 masala

import numpy as np
import matplotlib.pyplot as plt

# Boshlang‘ich shartlar
x0 = 0  # Boshlang‘ich x
y0 = 2  # Boshlang‘ich y
h = 0.2  # Qadam uzunligi
x_end = 1  # Oxirgi x

# Qadamlar soni
n_steps = int((x_end - x0) / h)  # 1 / 0.2 = 5 qadam

# x va y uchun massivlar
x_values = np.linspace(x0, x_end, n_steps + 1)  # [0, 0.2, 0.4, 0.6, 0.8, 1.0]
y_values = np.zeros(n_steps + 1)  # y qiymatlari uchun massiv
y_values[0] = y0  # Boshlang‘ich y

# Differentsial tenglama: y' = 3 + 2x - y
def f(x, y):
    return 3 + 2 * x - y

# Euler metodi
for i in range(n_steps):
    x_n = x_values[i]
    y_n = y_values[i]
    y_values[i + 1] = y_n + h * f(x_n, y_n)

# Natijalarni chiqarish
print("Euler metodi natijalari:")
for x, y in zip(x_values, y_values):
    print(f"x = {x:.1f}, y = {y:.4f}")

# Grafik chizish
plt.plot(x_values, y_values, 'o-', label='Euler metodi', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Euler metodi yordamida y(x) (1-savol)')
plt.grid(True)
plt.legend()
plt.show()


