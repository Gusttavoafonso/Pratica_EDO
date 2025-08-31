import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from Adams_Bashforth import adams


f = lambda t, y: -2*y
t0, y0 = 0, 1
h = 0.1
n_steps = 50
t_abm, y_abm = adams(f, t0, y0, h, n_steps)

# Solução exata
y_exact = np.exp(-2*t_abm)

# Solução SciPy 
sol = solve_ivp(f, [t0, t_abm[-1]], [y0], t_eval=t_abm, method="RK45")

#  Comparação
print("t     |   ABM2     |   SciPy(RK45)   |   Exato     |   |erro ABM|")
print("---------------------------------------------------------------")
for i in range(0, len(t_abm), 10):  # printa a cada 10 passos
    print(f"{t_abm[i]:5.2f} | {y_abm[i]:10.6f} | {sol.y[0][i]:13.6f} | {y_exact[i]:10.6f} | {abs(y_abm[i]-y_exact[i]):.2e}")

#  Gráfico
plt.plot(t_abm, y_exact, 'k-', label="Exato")
plt.plot(t_abm, y_abm, 'ro--', label="ABM2")
plt.plot(sol.t, sol.y[0], 'b^:', label="SciPy RK45")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Comparação: ABM2 x SciPy x Exato")
plt.legend()
plt.grid()
plt.show()