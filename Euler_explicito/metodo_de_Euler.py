import numpy as np
from typing import Callable, Iterable, Tuple

def euler_explicit(f: Callable[[float, np.ndarray], np.ndarray],
                   t0: float,
                   y0: Iterable[float] | float,
                   h: float,
                   n_steps: int) -> Tuple[np.ndarray, np.ndarray]:
    y0 = np.atleast_1d(np.array(y0, dtype=float))
    d = y0.size
    t = np.empty(n_steps + 1, dtype=float)
    y = np.empty((n_steps + 1, d), dtype=float)
    t[0] = t0
    y[0] = y0
    for k in range(n_steps):
        tk = t[k]
        yk = y[k]
        y[k + 1] = yk + h * np.atleast_1d(f(tk, yk))
        t[k + 1] = tk + h
    if d == 1:
        return t, y[:, 0]
    return t, y
