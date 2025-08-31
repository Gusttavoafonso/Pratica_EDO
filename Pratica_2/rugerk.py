import numpy as np



def rk4(f, t0, y0, h, n_steps):
    y0 = np.asarray(y0, dtype=float)
    if y0.ndim == 0:  # scalar case
        dim = 1
        y0 = np.array([y0])
        scalar_case = True
    else:
        dim = y0.shape[0]
        scalar_case = False

    t = np.zeros(n_steps + 1)
    y = np.zeros((n_steps + 1, dim))

    t[0] = t0
    y[0] = y0

    for k in range(n_steps):
        if scalar_case:
            k1 = np.array([f(t[k], y[k][0])])
            k2 = np.array([f(t[k] + h/2, y[k][0] + h*k1[0]/2)])
            k3 = np.array([f(t[k] + h/2, y[k][0] + h*k2[0]/2)])
            k4 = np.array([f(t[k] + h, y[k][0] + h*k3[0])])
        else:
            k1 = f(t[k], y[k])
            k2 = f(t[k] + h/2, y[k] + h*k1/2)
            k3 = f(t[k] + h/2, y[k] + h*k2/2)
            k4 = f(t[k] + h, y[k] + h*k3)

        y[k+1] = y[k] + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        t[k+1] = t[k] + h

    if scalar_case:
        return t, y[:, 0]
    return t, y
