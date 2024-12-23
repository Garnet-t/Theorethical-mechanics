#задание 18 рисунок 18
#назвние на моем компьютере 13_l2_6.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Параметры маятника
l = 1.0  # Длина стержня (м)
s = 0.2  # Смещение массы от точки подвеса (м)
L = l + s  # Полная длина маятника

# Углы маятника (от 30° до 0°)
angles_deg = np.linspace(30, 0, 100)  # 100 кадров анимации
angles_rad = np.radians(angles_deg)  # Преобразуем в радианы

# Точка подвеса
x0, y0 = 0, 0

# Настройка окна визуализации
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 0.5)
ax.set_aspect('equal')
ax.set_title("Движение маятника")
ax.set_xlabel("x (м)")
ax.set_ylabel("y (м)")

# Рисуем маятник: начальная линия и точка груза
line, = ax.plot([], [], 'o-', lw=2)  # Стержень маятника
mass, = ax.plot([], [], 'ro', markersize=8)  # Груз

# Функция инициализации для анимации
def init():
    line.set_data([], [])
    mass.set_data([], [])
    return line, mass

# Функция обновления кадров
def update(frame):
    # Текущий угол
    phi = angles_rad[frame]
    
    # Координаты груза
    x = L * np.sin(phi)
    y = -L * np.cos(phi)
    
    # Обновление линии и груза
    line.set_data([x0, x], [y0, y])
    mass.set_data([x],[y])
    return line, mass

# Создание анимации
ani = FuncAnimation(
    fig, update, frames=len(angles_rad), init_func=init, blit=True, interval=50
)

# Отображение
plt.show()
