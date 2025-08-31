from rugerk import rk4
import numpy as np


def adams(f, t0, y0, h, n_steps):
    y0 = np.asarray(y0, dtype=float)
    if y0.ndim == 0:  
        y0 = np.array([y0])
        scalar_case = True
    else:
        scalar_case = False
    
    t = np.zeros(n_steps+1)
    y = np.zeros((n_steps+1, len(y0)))
    t[0], y[0] = t0, y0

    # Usa RK4 para obter o ponto
    t_rk, y_rk = rk4(f, t0, y0[0] if scalar_case else y0, h, 1)
    if scalar_case:
        t[1], y[1] = t_rk[1], np.array([y_rk[1]])
    else:
        t[1], y[1] = t_rk[1], y_rk[1]

    # Iterações ABM
    for n in range(1, n_steps):
        # PREDITOR 
        if scalar_case:
            f_n = f(t[n], y[n][0])
            f_n1 = f(t[n-1], y[n-1][0])
            y_pred = y[n] + h/2 * (3*f_n - f_n1)
        else:
            y_pred = y[n] + h/2 * (3*f(t[n], y[n]) - f(t[n-1], y[n-1]))
        t[n+1] = t[n] + h
        # CORRETOR 
        if scalar_case:
            f_pred = f(t[n+1], y_pred[0])
            y[n+1] = y[n] + h/2 * (f_n + f_pred)
        else:
            y[n+1] = y[n] + h/2 * (f(t[n], y[n]) + f(t[n+1], y_pred))

    if scalar_case:
        return t, y[:, 0]
    return t, y