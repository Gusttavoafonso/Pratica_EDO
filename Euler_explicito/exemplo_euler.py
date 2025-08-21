import numpy as np
from math import exp
import matplotlib.pyplot as plt
from metodo_de_Euler import euler_explicit

def f(t, y):
    return -2.0 * y

# Euler explícito
t, y = euler_explicit(f, t0=0.0, y0=1.0, h=0.1, n_steps=50)

# Solução exata
y_exact = np.array([exp(-2 * ti) for ti in t])


error = np.abs(np.array(y) - y_exact)

print("\n=== Comparação Euler Explícito vs Solução Exata ===")
print(f"{'t':>6} | {'y_Euler':>12} | {'y_exato':>12} | {'Erro':>12}")
print("-"*50)
print(f"{t[-1]:6.2f} | {y[-1]:12.6f} | {y_exact[-1]:12.6f} | {error[-1]:12.6e}")
print("="*50)

# Plotagem
plt.figure(figsize=(10,6))
plt.plot(t, y, 'r-', label="Euler (h=0.1)")
plt.plot(t, y_exact, 'k--', label="Exato $e^{-2t}$")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Método de Euler Explícito: $y'=-2y$, $y(0)=1$")
plt.legend()
plt.grid(True)
plt.show()

# Plot do erro
plt.figure(figsize=(10,6))
plt.plot(t, error, 'b-', label="Erro absoluto")
plt.xlabel("t")
plt.ylabel("Erro |y - y_exato|")
plt.title("Erro do Método de Euler Explícito")
plt.grid(True)
plt.legend()
plt.show()
