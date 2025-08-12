# 📘 Métodos Numéricos para Problemas de Valor Inicial (PVI)

Este documento apresenta a formulação e aplicação de métodos numéricos clássicos para resolver **Problemas de Valor Inicial (PVI)** em **Equações Diferenciais Ordinárias (EDOs)**.

---

## 1️⃣ Método de Euler Explícito — PVI com uma EDO

### **Formulação**
Considere um PVI:

$$
y'(t) = f(t, y(t)), \quad y(t_0) = y_0
$$

O **método de Euler explícito** calcula:

$$
y_{n+1} = y_n + h \cdot f(t_n, y_n)
$$

onde:
- \( h \) é o passo,
- \( t_{n+1} = t_n + h \).

### **Algoritmo**
1. Defina \( t_0, y_0, h \) e \( N \) (número de passos).
2. Para \( n = 0, 1, \dots, N-1 \):
   - Calcule \( y_{n+1} = y_n + h \cdot f(t_n, y_n) \).

---

## 2️⃣ Método de Euler Explícito — PVI com Sistema de Duas EDO’s

### **Formulação**
Considere:

$$
\begin{cases}
y'(t) = f(t, y, z) \\
z'(t) = g(t, y, z) \\
y(t_0) = y_0, \quad z(t_0) = z_0
\end{cases}
$$

O método de Euler explícito:

$$
\begin{cases}
y_{n+1} = y_n + h \cdot f(t_n, y_n, z_n) \\
z_{n+1} = z_n + h \cdot g(t_n, y_n, z_n)
\end{cases}
$$

---

## 3️⃣ Método de Runge-Kutta de Quarta Ordem (RK4) — PVI com uma EDO

### **Formulação**
Para:

$$
y'(t) = f(t, y(t)), \quad y(t_0) = y_0
$$

O RK4 calcula:

$$
\begin{aligned}
k_1 &= f(t_n, y_n) \\
k_2 &= f\left(t_n + \frac{h}{2}, y_n + \frac{h}{2} k_1\right) \\
k_3 &= f\left(t_n + \frac{h}{2}, y_n + \frac{h}{2} k_2\right) \\
k_4 &= f\left(t_n + h, y_n + h k_3\right) \\
y_{n+1} &= y_n + \frac{h}{6} \left(k_1 + 2k_2 + 2k_3 + k_4\right)
\end{aligned}
$$

---

## 4️⃣ Método de Runge-Kutta de Quarta Ordem (RK4) — PVI com Sistema de Duas EDO’s

### **Formulação**
Para:

$$
\begin{cases}
y'(t) = f(t, y, z) \\
z'(t) = g(t, y, z) \\
y(t_0) = y_0, \quad z(t_0) = z_0
\end{cases}
$$

O RK4 calcula:

$$
\begin{aligned}
k_1^y &= f(t_n, y_n, z_n) \\
k_1^z &= g(t_n, y_n, z_n) \\
k_2^y &= f\left(t_n + \frac{h}{2}, y_n + \frac{h}{2} k_1^y, z_n + \frac{h}{2} k_1^z\right) \\
k_2^z &= g\left(t_n + \frac{h}{2}, y_n + \frac{h}{2} k_1^y, z_n + \frac{h}{2} k_1^z\right) \\
k_3^y &= f\left(t_n + \frac{h}{2}, y_n + \frac{h}{2} k_2^y, z_n + \frac{h}{2} k_2^z\right) \\
k_3^z &= g\left(t_n + \frac{h}{2}, y_n + \frac{h}{2} k_2^y, z_n + \frac{h}{2} k_2^z\right) \\
k_4^y &= f\left(t_n + h, y_n + h k_3^y, z_n + h k_3^z\right) \\
k_4^z &= g\left(t_n + h, y_n + h k_3^y, z_n + h k_3^z\right) \\
y_{n+1} &= y_n + \frac{h}{6} \left(k_1^y + 2k_2^y + 2k_3^y + k_4^y\right) \\
z_{n+1} &= z_n + \frac{h}{6} \left(k_1^z + 2k_2^z + 2k_3^z + k_4^z\right)
\end{aligned}
$$
