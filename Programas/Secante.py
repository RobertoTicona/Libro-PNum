import numpy as np
import matplotlib.pyplot as plt

# === 1. Ingreso de la función ===
func_str = input("Ingrese la función f(x): ")  # Ejemplo: x**3 - x - 1

# Definimos la función
def f(x):
    return eval(func_str, {"np": np, "x": x})

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

# === 3. Pregunta si desea aplicar el método de la secante ===
op = input("¿Desea encontrar una raíz con el método de la Secante? (s/n): ").lower()

if op == "s":
    # === 4. Ingreso de puntos iniciales ===
    x0 = float(input("Ingrese el primer valor inicial x0: "))
    x1 = float(input("Ingrese el segundo valor inicial x1: "))

    # Parámetros del método
    tol = 1e-6
    max_iter = 100

    print("\nIteración |     x0      |      x1      |     f(x0)     |     f(x1)     |     x2      |   Error")
    print("-------------------------------------------------------------------------------------------")

    for i in range(1, max_iter + 1):
        f0 = f(x0)
        f1 = f(x1)

        # Evitar división entre cero
        if f1 - f0 == 0:
            print(f"\n⚠️ División por cero en la iteración {i}. El método no puede continuar.")
            break

        # Fórmula del método de la secante
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)

        error = abs(x2 - x1)

        print(f"{i:9d} | {x0:10.6f} | {x1:10.6f} | {f0:12.6f} | {f1:12.6f} | {x2:10.6f} | {error:10.6f}")

        if error < tol:
            print(f"\n✅ Raíz aproximada encontrada: {x2:.6f}")
            print(f"Iteraciones realizadas: {i}")
            break

        # Actualización de los valores
        x0, x1 = x1, x2

    else:
        print("\n⚠️ No se alcanzó la convergencia después de", max_iter, "iteraciones.")
else:
    print("No se aplicó el método de la Secante.")
