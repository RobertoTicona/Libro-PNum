# Función para preparar expresiones lineales
def preparar_expresion(expr: str) -> str:
    expr = expr.replace(" ", "")          # quitar espacios
    expr = expr.replace("^", "**")        # potencia
    expr = expr.replace("-x", "-1*x")     # caso -x
    expr = expr.replace("+x", "+1*x")     # caso +x
    if expr.startswith("x"):              # si empieza con x
        expr = "1*" + expr
    expr = expr.replace("x", "*x")        # poner multiplicación
    expr = expr.replace("**x", "*x")      # corregir si se duplicó
    return expr

# Restricciones:
# 1) x = 5  (vertical)
# 2) x + y = 15  ->  y = -x + 15
func2 = preparar_expresion("-x+15")

# Rango de la gráfica
xmin, xmax = -5, 20
ymin, ymax = -5, 20

# Recorremos el plano
for y in range(ymax, ymin - 1, -1):
    linea = ""
    for x in range(xmin, xmax + 1):
        # Recta 1: x = 5
        cond1 = (x == 5)

        # Recta 2: y = -x + 15
        try:
            y2 = eval(func2)
        except:
            y2 = None
        cond2 = (y2 is not None and abs(y - y2) < 0.5)

        # Región factible: x>=5, y>=0, x+y<=15
        region = (x >= 5 and y >= 0 and x + y <= 15)

        # Qué dibujar
        if cond1 and cond2:
            linea += "#"
        elif cond1:
            linea += "*"
        elif cond2:
            linea += "o"
        elif x == 0 and y == 0:
            linea += "+"
        elif x == 0:
            linea += "|"
        elif y == 0:
            linea += "-"
        elif region:
            linea += "."
        else:
            linea += " "
    print(linea)

# Leyenda
print("\nLeyenda del gráfico:")
print("  * = x = 5")
print("  o = x + y = 15")
print("  # = Intersección")
print("  . = Región factible")
print("  | = Eje Y")
print("  - = Eje X")
print("  + = Origen (0,0)")
