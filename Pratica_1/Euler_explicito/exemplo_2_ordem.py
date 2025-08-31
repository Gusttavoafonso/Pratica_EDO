import numpy as np
import matplotlib.pyplot as plt
from metodo_Euler_2_ordem import euler_explicit_2nd
import sympy as sp

def f(t, y, dy):
    return np.cos(2*t) - 0.5*dy - y

# parâmetros
t0, y0, dy0 = 0, 1, 0   # condições iniciais
h = 0.1                 # passo
n_steps = 100           # número de passos

# solução numérica
t, y_num, dy_num = euler_explicit_2nd(f, t0, y0, dy0, h, n_steps)

# ======================
# Solução exata simbólica com sympy
# ======================
t_sym = sp.symbols('t')
y = sp.Function('y')

# Define EDO: y'' + 0.5 y' + y = cos(2t)
ode = sp.Eq(sp.diff(y(t_sym), t_sym, 2) + 0.5*sp.diff(y(t_sym), t_sym) + y(t_sym),
             sp.cos(2*t_sym))

# Resolve com as condições iniciais
sol = sp.dsolve(ode, ics={y(0): y0, sp.diff(y(t_sym), t_sym).subs(t_sym, 0): dy0})

# Transforma em função numérica para avaliação
y_exact_func = sp.lambdify(t_sym, sol.rhs, 'numpy')
y_exact = y_exact_func(t)

# ======================
# Gráfico comparação
# ======================
plt.figure(figsize=(10,5))
plt.plot(t, y_exact, label="Solução exata (sympy)")
plt.plot(t, y_num, linestyle="--", label="Euler explícito (2ª ordem)")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("PVI: y'' + 0.5y' + y = cos(2t)")
plt.legend()
plt.grid(True)
plt.show()

# ======================
# Gráfico do erro absoluto
# ======================
plt.figure(figsize=(10,5))
plt.plot(t, np.abs(y_num - y_exact), label="Erro absoluto")
plt.xlabel("t")
plt.ylabel("|y_num - y_exato|")
plt.title("Erro absoluto ao longo do tempo (Euler explícito)")
plt.legend()
plt.grid(True)
plt.show()
