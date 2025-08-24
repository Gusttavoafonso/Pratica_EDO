import numpy as np
from typing import Callable, Iterable, Tuple

def rk4(f, t0: float, y0, h: float, n_steps: int):
    y0 = np.atleast_1d(np.array(y0, dtype=float))
    d = y0.size
    t = np.empty(n_steps + 1, dtype=float)
    y = np.empty((n_steps + 1, d), dtype=float)
    t[0] = t0
    y[0] = y0
    for k in range(n_steps):
        tk = t[k]; yk = y[k]
        k1 = np.atleast_1d(f(tk, yk))
        k2 = np.atleast_1d(f(tk + h/2.0, yk + (h/2.0)*k1))
        k3 = np.atleast_1d(f(tk + h/2.0, yk + (h/2.0)*k2))
        k4 = np.atleast_1d(f(tk + h,       yk +  h      *k3))
        y[k+1] = yk + (h/6.0)*(k1 + 2.0*k2 + 2.0*k3 + k4)
        t[k+1] = tk + h
    if d == 1:
        return t, y[:, 0]
    return t, y