from math import exp
import matplotlib.pyplot as plt
from metodo_de_Euler import euler_explicit

def f(t, y):
    return -2.0 * y

t, y = euler_explicit(f, t0=0.0, y0=1.0, h=0.1, n_steps=50)

y_exact = [exp(-2 * ti) for ti in t]

# Print last point and compare with exact
print(f"t_final = {t[-1]:.2f}, y_Euler = {y[-1]:.6f}, y_exato = {exp(-2*t[-1]):.6f}")

# Plotagem
plt.plot(t, y, label="Euler (h=0.1)")
plt.plot(t, y_exact, '--', label="Exato $e^{-2t}$")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Método de Euler Explícito: $y'=-2y$, $y(0)=1$")
plt.legend()
plt.grid(True)
plt.show()