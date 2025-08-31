import numpy as np



def rk4(f, t0, y0, h, n_steps):

    t = np.zeros(n_steps + 1)
    y = np.zeros(n_steps + 1)

    t[0] = t0
    y[0] = y0

    for k in range(n_steps):
        k1 = f(t[k], y[k])
        k2 = f(t[k] + h/2, y[k] + h*k1/2)
        k3 = f(t[k] + h/2, y[k] + h*k2/2)
        k4 = f(t[k] + h, y[k] + h*k3)

        y[k+1] = y[k] + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        t[k+1] = t[k] + h

    return t, y
