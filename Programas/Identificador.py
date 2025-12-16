import re

def analizar_funcion(funcion):
    funcion = funcion.replace(" ", "")
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
    print(f"\n   Función ingresada: {funcion}")
    print(f"   Variables encontradas: {variables}")
    print(f"   Términos: {terminos}")
    print(f"   Coeficientes: {coeficientes}")
    print(f"   Signos: {signos}")

print("=== ANALIZADOR DE FUNCIONES ALGEBRAICAS ===")
funcion = input("   Ingresa una función (ejemplo: 3x^2 - 4x + 7): ")
analizar_funcion(funcion)
