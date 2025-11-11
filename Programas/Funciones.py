import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# === Ingreso de la función por el usuario ===
expr_str = input("Ingrese la función en términos de x (ejemplo: sin(x), x**2 + 3*x - 5, exp(-x)*cos(x)): ")

# === Definición de variable simbólica ===
x = sp.Symbol('x')

# === Conversión del texto a expresión simbólica ===
try:
    expr = sp.sympify(expr_str)
except sp.SympifyError:
    print("Error: la función ingresada no es válida.")
    exit()

# === Creación de función numérica evaluable ===
f = sp.lambdify(x, expr, modules=['numpy'])

# === Intervalo de graficación ===
x_vals = np.linspace(-10, 10, 400)
y_vals = f(x_vals)

# === Graficar ===
plt.figure(figsize=(7,5))
plt.plot(x_vals, y_vals, label=f"$f(x) = {sp.latex(expr)}$", color='navy')
plt.title("Gráfica de la función ingresada", fontsize=13)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.legend()
plt.show()
