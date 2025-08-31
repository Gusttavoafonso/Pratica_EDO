import numpy as np
import matplotlib.pyplot as plt
from rugerK2_ordem import rk4_2ordem

# Sistema: y1' = y2, y2' = -omega^2 y1 
omega = 1.0

def f_system(t, y):
    y1, y2 = y
    return np.array([y2, -(omega**2)*y1])
    

# Parâmetros
t0 = 0.0
y0 = np.array([1.0, 0.0])
h = 0.02
n_steps = 800  # t_final = 16

# RK4
t, Y = rk4_2ordem(f_system, t0=t0, y0=y0, h=h, n_steps=n_steps)
y1, y2 = Y[:, 0], Y[:, 1]

# Solução exata
y1_exact = np.cos(omega * t)
y2_exact = -np.sin(omega * t)

# Print organizado
print("\n=== Comparação no ponto final (sistema 2D) ===")
print(f"{'Componente':<12} | {'RK4':>12} | {'Exato':>12} | {'|erro|':>12}")
print("-"*57)
print(f"{'y1(t_f)':<12} | {y1[-1]:>12.6f} | {y1_exact[-1]:>12.6f} | {abs(y1[-1]-y1_exact[-1]):>12.2e}")
print(f"{'y2(t_f)':<12} | {y2[-1]:>12.6f} | {y2_exact[-1]:>12.6f} | {abs(y2[-1]-y2_exact[-1]):>12.2e}")
print("="*57)

# Gráfico
plt.plot(t, y1, label="y1 (RK4)")
plt.plot(t, y2, label="y2 (RK4)")
plt.plot(t, y1_exact, "--", label="y1 exato")
plt.plot(t, y2_exact, "--", label="y2 exato")
plt.xlabel("t")
plt.ylabel("y1(t), y2(t)")
plt.title("Sistema de duas EDOs com RK4")
plt.legend()
plt.tight_layout()
plt.show()
