# Graficar restricciones del problema 3 en ASCII con sombreado de la región factible

xmin, xmax = 0, 14
ymin, ymax = 0, 14

for y in range(ymax, ymin - 1, -1):
    linea = ""
    for x in range(xmin, xmax + 1):

        # Restricciones
        cond_recta = (abs(x + y - 12) < 0.5)   # frontera x+y=12
        cond_x = (x == 4)                      # frontera x=4
        cond_y = (y == 6)                      # frontera y=6

        # Región factible: x>=4, y>=6, x+y<=12
        cond_region = (x >= 4 and y >= 6 and (x + y <= 12))

        # Puntos de intersección (vértices)
        vertices = [(4,6), (4,8), (6,6)]
        cond_vertice = (x,y) in vertices

        # Dibujar con prioridad
        if cond_vertice:
            linea += "#"
        elif cond_region:
            linea += "o"
        elif cond_recta:
            linea += "*"
        elif cond_x:
            linea += "|"
        elif cond_y:
            linea += "="
        elif x == 0 and y == 0:
            linea += "+"
        elif x == 0:
            linea += "|"
        elif y == 0:
            linea += "-"
        else:
            linea += " "
    print(linea)

print("\nLeyenda:")
print("  * = Frontera x+y=12")
print("  | = Frontera x=4")
print("  = = Frontera y=6")
print("  # = Vértices de la región factible")
print("  o = Región factible (sombreada)")
print("  + = Origen")
print("  - , | = Ejes coordenados")