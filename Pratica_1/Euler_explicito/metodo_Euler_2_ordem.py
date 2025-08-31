import numpy as np
from typing import Callable, Tuple

def euler_explicit_2nd(f: Callable[[float, float, float], float],
                       t0: float,
                       y0: float,
                       dy0: float,
                       h: float,
                       n_steps: int) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:


    # Vetores de saída
    t = np.empty(n_steps + 1, dtype=float)
    y = np.empty(n_steps + 1, dtype=float)
    dy = np.empty(n_steps + 1, dtype=float)

    # Condições iniciais
    t[0] = t0
    y[0] = y0
    dy[0] = dy0

    # Iterações de Euler
    for k in range(n_steps):
        t[k + 1] = t[k] + h
        y[k + 1] = y[k] + h * dy[k]
        dy[k + 1] = dy[k] + h * f(t[k], y[k], dy[k])

    return t, y, dy
