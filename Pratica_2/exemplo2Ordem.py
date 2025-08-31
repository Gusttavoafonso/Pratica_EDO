import matplotlib.pyplot as plt
import numpy as np
from Adams_2_ordem import adams    


def _oscillator(t: float, y: np.ndarray) -> np.ndarray:
    """Sistema do oscilador harmônico: y1' = y2, y2' = -y1."""
    y1, y2 = y
    return np.array([y2, -y1], dtype=float)


# Parâmetros
t0 = 0.0
y0 = np.array([1.0, 0.0], dtype=float)  # solução exata: y1=cos(t), y2=-sin(t)
tf = 20.0
n_steps = 2000
h = (tf - t0) / n_steps

# Resolver
T, Y = adams(_oscillator, t0, y0, h, n_steps=n_steps)

# Solução exata
y1_exact = np.cos(T)
y2_exact = -np.sin(T)

# Erro
err = np.sqrt((Y[:, 0] - y1_exact)**2 + (Y[:, 1] - y2_exact)**2)

print(f"Passo h = {h:.6f}, max erro L2 ≈ {np.max(err):.3e}")
print("t, y1_num, y2_num (primeiros 5):")
for i in range(5):
    print(f"{T[i]:.3f}, {Y[i,0]:+.6f}, {Y[i,1]:+.6f}")

# Gráficos
plt.figure()
plt.plot(T, y1_exact, label="y1 exato")
plt.plot(T, Y[:, 0], "--", label="y1 ABM4")
plt.xlabel("t")
plt.ylabel("y1")
plt.title("Oscilador harmônico: y1(t) — ABM4 vs exato")
plt.legend()
plt.grid(alpha=0.3)
plt.show()