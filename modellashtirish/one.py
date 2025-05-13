
# 2.1-masala

# bu masalani ishlashdan maqsad shuki 

# Qanday qilib mashinalarni shunday yuklaymizki, materiallar ehtiyoji qondiriladi va 
# umumiy xarajat minimal bo‘lsin?

from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus, value
import matplotlib.pyplot as plt
# Ma'lumotlar
materials = [1, 2, 3, 4, 5]  # 5 xil material 
machines = [1, 2, 3, 4]  # 4 xil mashina

# Material ehtiyojlari
M = {1:800, 2:950, 3:620, 4:200, 5:580}

# Mashinalar vaqt cheklovlari (soat)
T = {1:365, 2:412, 3:211, 4:524}

# Jadvaldan vaqt va xarajat ma'lumotlari
# t_ij va c_ij
time = {
    (1,1):0.024, (1,2):0.041, (1,3):0.012, (1,4):0.041, (1,5):0.019,
    (2,1):0.022, (2,2):0.038, (2,3):0.015, (2,4):0.033, (2,5):0.028,
    (3,1):0.014, (3,2):0.045, (3,3):0.026, (3,4):0.022, (3,5):0.01,
    (4,1):0.023, (4,2):0.016, (4,3):0.02, (4,4):0.016, (4,5):0.033
}

cost = {
    (1,1):150, (1,2):210, (1,3):108, (1,4):164, (1,5):265,
    (2,1):85, (2,2):105, (2,3):321, (2,4):93, (2,5):93,
    (3,1):287, (3,2):65, (3,3):95, (3,4):259, (3,5):187,
    (4,1):311, (4,2):247, (4,3):327, (4,4):129, (4,5):545
}

# 1. Model yaratamiz
model = LpProblem("Optimal_uskunalar_yuklash", LpMinimize)

# 2. O'zgaruvchilar: x_ij
x = LpVariable.dicts("x", [(i,j) for i in machines for j in materials], lowBound=0)

# 3. Maqsad funksiyasi
"""
Maqsad funksiyasi qo‘shildi: umumiy xarajatni minimallashtirish
"""
model += lpSum(cost[(i,j)] * x[(i,j)] for i in machines for j in materials) 


# 4. Material ehtiyojlari sharti
"""
Har material uchun umumiy ishlab chiqarilgan miqdor = kerakli ehtiyoj
"""
for j in materials:
    model += lpSum(x[(i,j)] for i in machines) == M[j]

# 5. Mashina vaqt cheklovlari
"""
Har mashina uchun umumiy ishlash vaqti ≤ maksimal vaqt
"""
for i in machines:
    model += lpSum(time[(i,j)] * x[(i,j)] for j in materials) <= T[i]

# 6. Modelni yechamiz
"""
Modelni yechish (optimal yechim topish
"""
model.solve()

# 7. Natijalar
"""
Har mashina-material juftligi uchun qancha ishlash kerakligini chiqaradi
"""
print("Holat:", LpStatus[model.status])
print("\nFaqat ishlatilgan mashina-material juftliklari:")
for i in machines:
    for j in materials:
        if x[(i,j)].varValue > 0:
            print(f"x[{i},{j}] = {x[(i,j)].varValue:.2f} m3")

print("\nUmumiy xarajat:", value(model.objective))

# 8. Vizualizatsiya: Har bir mashinaning ish vaqti
machines_load = {i: sum(time[(i,j)] * x[(i,j)].varValue for j in materials) for i in machines}
plt.figure(figsize=(8, 6))
plt.bar(machines_load.keys(), machines_load.values(), color='skyblue')
plt.xlabel('Mashinalar')
plt.ylabel('Ish vaqti (soat)')
plt.title('Mashinalar bo‘yicha ish yuki')
plt.xticks(list(machines))  # Mashina raqamlari X o‘qida
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()