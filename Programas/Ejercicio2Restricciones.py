# Restricción principal: 3x + 5y <= 20  →  y <= (20 - 3x)/5
func = "(20 - 3*x)/5"

# Definimos el rango del gráfico (valores de X y Y)
xmin, xmax = -1, 10     # un poco más para ver bien
ymin, ymax = -1, 6

# Recorremos los valores de Y de arriba hacia abajo
for y in range(ymax, ymin - 1, -1):
    linea = ""

    for x in range(xmin, xmax + 1):
        try:
            y_line = eval(func)
        except:
            y_line = None

        # Condición para la recta
        cond_line = (y_line is not None and abs(y - y_line) < 0.5)

        # Condición para la región factible: debajo de la recta y en el primer cuadrante
        cond_region = (y_line is not None and y <= y_line and x >= 0 and y >= 0)

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
print("  * = Recta 3x + 5y = 20 (frontera)")
print("  o = Región factible (3x + 5y <= 20, x>=0, y>=0)")
print("  | = Eje Y")
print("  - = Eje X")
print("  + = Origen (0,0)")