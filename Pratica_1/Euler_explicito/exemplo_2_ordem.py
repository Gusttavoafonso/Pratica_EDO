import numpy as np
import matplotlib.pyplot as plt
from metodo_de_Euler import euler_explicit 


# --- Definição do sistema ---
omega = 1.0
def f_system(t, y):
    y1, y2 = y
    return np.array([y2, -(omega**2) * y1])

# Parâmetros
t0 = 0.0
y0 = np.array([1.0, 0.0])
h = 0.02
n_steps = 800
t_final = t0 + n_steps * h

#  Cálculo usando a SUA função euler_explicit ---
t_custom, Y_custom = euler_explicit(f_system, t0=t0, y0=y0, h=h, n_steps=n_steps)
y1_custom = Y_custom[:, 0]
y2_custom = Y_custom[:, 1]

# --- Solução exata ---
y1_exact = np.cos(omega * t_custom)

# --- Print comparando com a solução exata ---
print("\n=== Comparação no ponto final: Euler explícito vs. Solução exata ===")
print(f"{'Componente':<12} | {'Euler':>12} | {'Exato':>12}")
print("-"*40)
print(f"{'y1(t_f)':<12} | {y1_custom[-1]:>12.6f} | {y1_exact[-1]:>12.6f}")
print(f"{'y2(t_f)':<12} | {y2_custom[-1]:>12.6f} | {(-np.sin(omega*t_custom[-1])):>12.6f}")
print("="*40)

# --- Gráfico ---
plt.figure(figsize=(12, 7))
plt.plot(t_custom, y1_custom, 'r-', label="y1 (Euler explícito)", linewidth=2)
plt.plot(t_custom, y1_exact, 'k--', label="y1 (Exato)", linewidth=2)
plt.xlabel("Tempo (t)")
plt.ylabel("y1(t)")
plt.title("Comparação Euler Explícito vs Solução Exata")
plt.legend()
plt.grid(True)
plt.show()