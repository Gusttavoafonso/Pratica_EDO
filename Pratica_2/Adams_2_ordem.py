from typing import Callable, Tuple
import numpy as np
from rugerK2_ordem import rk4_2ordem


# Método ABM4  para resolver um sistema de 2 EDOs
def adams(
    f: Callable[[float, np.ndarray], np.ndarray],  
    t0: float,         # instante inicial
    y0: np.ndarray,     # condição inicial (vetor com 2 componentes)
    h: float,             # passo
    n_steps: int,         # número de passos
    max_corrections: int = 2, # n máx. de iterações no corretor 
    tol: float = 1e-12,      # tolerância para convergência do corretor
) -> Tuple[np.ndarray, np.ndarray]:

    # Garante que y0 é um vetor numpy do tipo float
    y0 = np.asarray(y0, dtype=float)

    # Só aceita sistemas com exatamente 2 variáveis
    if y0.shape != (2,):
        raise ValueError("y0 deve ter shape (2,) para duas EDO's.")

    # Arrays para armazenar a solução
    T = np.empty(n_steps + 1, dtype=float)    # instantes de tempo
    Y = np.empty((n_steps + 1, 2), dtype=float)  # soluções (y1, y2) em cada instante
    F = np.empty((n_steps + 1, 2), dtype=float)  # valores f(t_i, y_i) já avaliados

    # Inicialização
    T[0] = t0
    Y[0] = y0
    F[0] = f(T[0], Y[0])

    # usa RK4 para obter as 3 primeiras soluções (Y[1], Y[2], Y[3])
    for i in range(3):
        T[i+1] = T[i] + h
        _, y_temp = rk4_2ordem(f, T[i], Y[i], h, 1)  # aplica 1 passo de RK4
        Y[i+1] = y_temp[1]  # pega o último valor de y retornado
        F[i+1] = f(T[i+1], Y[i+1])

    # Loop principal do ABM4 
    for n in range(3, n_steps):
        T[n+1] = T[n] + h

        #Preditor: (explícito) 
        fp = 55*F[n] - 59*F[n-1] + 37*F[n-2] - 9*F[n-3]
        y_pred = Y[n] + (h/24.0)*fp

        #  Corretor: (implícito)
        y_new = y_pred.copy()
        for _ in range(max_corrections):
            f_np1 = f(T[n+1], y_new)
            y_next = Y[n] + (h/24.0)*(9*f_np1 + 19*F[n] - 5*F[n-1] + F[n-2])
            
            # Critério de parada: se convergiu, para as iterações
            if np.linalg.norm(y_next - y_new, ord=np.inf) < tol:
                y_new = y_next
                break
            y_new = y_next  

        
        Y[n+1] = y_new
        F[n+1] = f(T[n+1], Y[n+1])

    return T, Y