
# 5.3 masala.
"""

Ushbu nuqtalar orqali o‘tadigan interpolatsion polinomni toping.

"""

import numpy as np
import matplotlib.pyplot as plt

# Berilgan nuqtalar
x_points = np.array([-1, 0, 1, 2, 4])
y_points = np.array([-2, -1, 1, 3, 7])

# Lagranj interpolatsiyasi funksiyasi
def lagrange_interpolation(x_points, y_points, x):
    n = len(x_points)
    result = 0
    for i in range(n):
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += y_points[i] * L_i
    return result

# Grafik uchun x va y qiymatlari
x_values = np.linspace(-2, 5, 100)
y_values = np.array([lagrange_interpolation(x_points, y_points, x) for x in x_values])

# Polinom koeffitsientlarini topish
coeffs = np.polyfit(x_points, y_points, 3)  # 3-darajali polinom
a, b, c, d = coeffs
print(f"Polinom: P(x) = {a:.3f}x^3 + {b:.3f}x^2 + {c:.3f}x + {d:.3f}")

# Grafik chizish
plt.plot(x_values, y_values, label='Lagranj interpolatsion polinomi', color='blue')
plt.scatter(x_points, y_points, color='red', label='Berilgan nuqtalar')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lagranj interpolatsion polinomi (1-savol)')
plt.grid(True)
plt.legend()
plt.show()