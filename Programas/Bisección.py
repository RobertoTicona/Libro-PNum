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

# === 3. Pregunta si desea aplicar el método de bisección ===
op = input("¿Desea encontrar una raíz con el método de Bisección? (s/n): ").lower()

if op == "s":
    # === 4. Ingreso del intervalo inicial ===
    a = float(input("Ingrese el extremo izquierdo del intervalo (a): "))
    b = float(input("Ingrese el extremo derecho del intervalo (b): "))

    # Verificación del cambio de signo
    if f(a) * f(b) > 0:
        print("\n⚠️ No hay cambio de signo en el intervalo [a, b]. Intente con otro intervalo.")
    else:
        # Parámetros del método
        tol = 1e-6
        max_iter = 100

        print("\nIteración |     a       |      b       |      c       |    f(c)     |   Error")
        print("--------------------------------------------------------------------------")

        for i in range(1, max_iter + 1):
            c = (a + b) / 2
            fc = f(c)

            # Calcular error (mitad del intervalo)
            error = abs(b - a) / 2

            print(f"{i:9d} | {a:10.6f} | {b:10.6f} | {c:10.6f} | {fc:10.6f} | {error:10.6f}")

            if abs(fc) < tol or error < tol:
                print(f"\n✅ Raíz aproximada encontrada: {c:.6f}")
                print(f"Iteraciones realizadas: {i}")
                break

            # Verificar cambio de signo
            if f(a) * fc < 0:
                b = c
            else:
                a = c
        else:
            print("\n⚠️ No se alcanzó la convergencia después de", max_iter, "iteraciones.")
else:
    print("No se aplicó el método de Bisección.")
