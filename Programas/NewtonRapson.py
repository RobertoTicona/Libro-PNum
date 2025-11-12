import numpy as np
import matplotlib.pyplot as plt

# === 1. Ingreso de la función ===
func_str = input("Ingrese la función f(x): ")  # Ejemplo: x**3 - x - 1

# Definimos la función y su derivada (usando derivada numérica)
def f(x):
    return eval(func_str)

def f_prime(x, h=1e-6):  # derivada numérica
    return (f(x + h) - f(x - h)) / (2 * h)

# === 2. Graficar la función ===
xmin = float(input("Ingrese el valor mínimo de x: "))
xmax = float(input("Ingrese el valor máximo de x: "))

x = np.linspace(xmin, xmax, 400)
y = f(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label=f"f(x) = {func_str}", color='blue')
plt.axhline(0, color='black', linestyle='--')
plt.axvline(0, color='black', linestyle='--')
plt.title("Gráfico de la función ingresada")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()

# === 3. Pregunta si desea aplicar Newton-Raphson ===
op = input("¿Desea encontrar una raíz con el método de Newton-Raphson? (s/n): ").lower()

if op == "s":
    # === 4. Ingreso de punto inicial ===
    x0 = float(input("Basado en la gráfica, ingrese el valor inicial x1: "))

    # Parámetros del método
    tol = 1e-6
    max_iter = 100

    # Iteraciones
    for i in range(1, max_iter + 1):
        fx = f(x0)
        fpx = f_prime(x0)

        if fpx == 0:
            print(f"La derivada es cero en x = {x0}. El método no puede continuar.")
            break

        x1 = x0 - fx / fpx

        # Verificar convergencia
        if abs(x1 - x0) < tol:
            print(f"\n✅ Raíz aproximada encontrada: {x1:.6f}")
            print(f"Iteraciones realizadas: {i}")
            break

        x0 = x1
    else:
        print("\n⚠️ No se alcanzó la convergencia después de", max_iter, "iteraciones.")

else:
    print("No se aplicó el método de Newton-Raphson.")
