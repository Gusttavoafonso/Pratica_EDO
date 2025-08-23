import numpy as np
import matplotlib.pyplot as plt
from math import exp
from rugerk import rk4


#Exemplo
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
