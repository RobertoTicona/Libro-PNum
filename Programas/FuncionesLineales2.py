import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def graficar():
    x = np.linspace(-10, 10, 100)
    y1 = 2 * x + 3
    y2 = -1 * x + 5

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x, y1, label='f₁(x) = 2x + 3', linewidth=2)
    ax.plot(x, y2, label='f₂(x) = -x + 5', linewidth=2)

    ax.set_title("Gráfico de dos funciones lineales")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.axhline(0)
    ax.axvline(0)
    ax.grid(True)
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)

ventana = tk.Tk()
ventana.title("Gráfico de funciones lineales")
ventana.geometry("700x500")

titulo = tk.Label(
    ventana,
    text="GRÁFICO DE FUNCIONES LINEALES",
    font=("Arial", 14, "bold")
)
titulo.pack(pady=10)

boton = tk.Button(
    ventana,
    text="Mostrar gráfica",
    font=("Arial", 11),
    command=graficar
)
boton.pack(pady=5)

ventana.mainloop()
