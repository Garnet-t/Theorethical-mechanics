#на моем компьютере 14_11.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

# Константы
g = 9.81  # Ускорение свободного падения, м/с^2
l =  0.5   # Длина стержня, м
mu = 0.2  # Коэффициент трения
k = 10.0   # Коэффициент жесткости
m = 1.0   # Масса тела, кг
P = m * g  # Вес тела, Н (P = m * g)

# Уравнения движения
def equations(t, y):
    s, s_dot, phi, phi_dot = y
    s_ddot = -mu * g * s_dot / P - k * g * s / P + phi_dot**2 * (l + s) + g * np.cos(phi)
    phi_ddot = -(2 * s_dot * phi_dot + g * np.sin(phi)) / (l + s)
    return [s_dot, s_ddot, phi_dot, phi_ddot]

# Начальные условия: [s, s_dot, phi, phi_dot]
y0 = [0.1, 0,  np.pi / 6, 0]  # Начальная длина, скорость, угол (рад), угловая скорость

# Временной интервал
t_span = (0, 10)
t_eval = np.linspace(*t_span, 500)

# Решение системы
sol = solve_ivp(equations, t_span, y0, t_eval=t_eval)

# Извлечение данных
s = sol.y[0]
phi = sol.y[2]
length = l + s
x = length * np.sin(phi)  # X-координата
y = -length * np.cos(phi)  # Y-координата

# Анимация
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.set_title("Анимация движения системы")
ax.set_xlabel("X (м)")
ax.set_ylabel("Y (м)")

# Элементы анимации
rod, = ax.plot([], [], 'k-', lw=2)  # стержень
mass, = ax.plot([], [], 'ro', markersize=10)  # груз

# Обновление кадров для анимации
def update(frame):
    rod.set_data([0, x[frame]], [0, y[frame]])  # обновление стержня
    mass.set_data([x[frame]], [y[frame]])  # обновление положения груза
    return rod, mass

# Создание анимации
ani = FuncAnimation(fig, update, frames=len(t_eval), interval=20, blit=True)

# Запуск анимации
plt.show()
