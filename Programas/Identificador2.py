import re
import tkinter as tk
from tkinter import messagebox

def analizar_funcion():
    funcion = entrada_funcion.get().replace(" ", "")

    if not funcion:
        messagebox.showwarning("Advertencia", "Ingrese una función algebraica")
        return

    variables = sorted(set(re.findall(r'[a-zA-Z]', funcion)))
    terminos = re.findall(r'[+-]?\d*[a-zA-Z]?\^?\d*', funcion)
    terminos = [t for t in terminos if t]

    coeficientes = []
    signos = []

    for t in terminos:
        if t.startswith('-'):
            signos.append('-')
        else:
            signos.append('+')

        c = re.findall(r'[+-]?\d+', t)
        if c:
            coef = int(c[0])
        else:
            coef = -1 if t.startswith('-') else 1

        coeficientes.append(coef)

    salida.config(state="normal")
    salida.delete("1.0", tk.END)
    salida.insert(tk.END, f"   Función ingresada: {funcion}\n")
    salida.insert(tk.END, f"   Variables encontradas: {variables}\n")
    salida.insert(tk.END, f"   Términos: {terminos}\n")
    salida.insert(tk.END, f"   Coeficientes: {coeficientes}\n")
    salida.insert(tk.END, f"   Signos: {signos}\n")
    salida.config(state="disabled")

ventana = tk.Tk()
ventana.title("Analizador de Funciones Algebraicas")
ventana.geometry("500x400")
ventana.resizable(False, False)

titulo = tk.Label(
    ventana,
    text="ANALIZADOR DE FUNCIONES ALGEBRAICAS",
    font=("Arial", 14, "bold")
)
titulo.pack(pady=10)

label_funcion = tk.Label(
    ventana,
    text="Ingrese la función (ejemplo: 3x^2 - 4x + 7):"
)
label_funcion.pack()

entrada_funcion = tk.Entry(
    ventana,
    width=40,
    font=("Arial", 12)
)
entrada_funcion.pack(pady=5)

boton = tk.Button(
    ventana,
    text="Analizar función",
    font=("Arial", 11),
    command=analizar_funcion
)
boton.pack(pady=10)

salida = tk.Text(
    ventana,
    height=10,
    width=55,
    state="disabled",
    font=("Consolas", 10)
)
salida.pack(pady=10)

ventana.mainloop()


