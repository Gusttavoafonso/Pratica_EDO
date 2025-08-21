import numpy as np
import matplotlib.pyplot as plt
from math import exp

def rk4(f, t0, y0, h, n_steps):
    """
    Método de Runge-Kutta de quarta ordem (RK4) para resolver
    y'(t) = f(t, y), y(t0) = y0

    Retorna:
        t : array com os pontos no tempo
        y : array com as aproximações de y(t)
    """
    t = np.zeros(n_steps + 1)
    y = np.zeros(n_steps + 1)

    t[0] = t0
    y[0] = y0

    for k in range(n_steps):
        k1 = f(t[k], y[k])
        k2 = f(t[k] + h/2, y[k] + h*k1/2)
        k3 = f(t[k] + h/2, y[k] + h*k2/2)
        k4 = f(t[k] + h, y[k] + h*k3)

        y[k+1] = y[k] + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        t[k+1] = t[k] + h

    return t, y

# --- Exemplo ---
# y' = -2y, y(0) = 1, solução exata y(t) = e^{-2t}
def f(t, y):
    return -2*y

t0 = 0
y0 = 1
h = 0.1
n_steps = 50

t, y_rk4 = rk4(f, t0, y0, h, n_steps)

# Solução exata
y_exact = np.exp(-2*t)

# Print no ponto final
print("\n=== Comparação no ponto final ===")
print(f"{'Método':<10} | {'y(t_final)':>12}")
print("-"*25)
print(f"{'RK4':<10} | {y_rk4[-1]:>12.6f}")
print(f"{'Exato':<10} | {y_exact[-1]:>12.6f}")
print("="*25)

# Plot
plt.plot(t, y_rk4, "o-", label="RK4 (h=0.1)")
plt.plot(t, y_exact, "--", label="Exato $e^{-2t}$")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Método de Runge-Kutta 4ª ordem")
plt.legend()
plt.grid(True)
plt.show()
