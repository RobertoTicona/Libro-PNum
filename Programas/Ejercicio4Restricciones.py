# Problema 4 - Modelos 3D y Texturas

# Definimos el rango del gráfico
xmin, xmax = -1, 12
ymin, ymax = -1, 8

# Recorremos los valores de Y de arriba hacia abajo
for y in range(ymax, ymin - 1, -1):
    linea = ""

    for x in range(xmin, xmax + 1):

        # Ecuación de la frontera: 2x + 3y = 18
        y_line = (18 - 2*x) / 3 if (18 - 2*x) >= 0 else None

        # Condición para estar en la recta
        cond_line = (y_line is not None and abs(y - y_line) < 0.5)

        # Condición para estar en la región factible
        cond_region = (x >= 0 and y >= 0 and (2*x + 3*y <= 18))

        if cond_line:
            linea += "*"
        elif cond_region:
            linea += "o"
        elif x == 0 and y == 0:
            linea += "+"
        elif x == 0:
            linea += "|"
        elif y == 0:
            linea += "-"
        else:
            linea += " "
    print(linea)

# Leyenda
print("\nLeyenda del gráfico:")
print("  * = Frontera 2x + 3y = 18")
print("  o = Región factible (2x + 3y <= 18, x>=0, y>=0)")
print("  | = Eje Y")
print("  - = Eje X")
print("  + = Origen (0,0)")