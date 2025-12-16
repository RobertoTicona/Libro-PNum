# Importar librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import linalg
import pandas as pd

# Configuración de visualización
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10
sns.set_style("whitegrid")

print("Librerías importadas correctamente")
print(f"NumPy versión: {np.__version__}")

# Definición de servicios médicos
servicios = [
    'Emergencia\n(Dieta líquida)',
    'Medicina Interna\n(Dieta blanda)',
    'Cirugía\n(Dieta progresiva)',
    'Alta hospitalaria'
]

n_servicios = len(servicios)

# Matriz de transición inicial
# T[i,j] = probabilidad de pasar del servicio i al servicio j
T_inicial = np.array([
    [0.20, 0.45, 0.25, 0.10],  # Desde Emergencia
    [0.05, 0.40, 0.25, 0.30],  # Desde Medicina Interna
    [0.05, 0.15, 0.50, 0.30],  # Desde Cirugía
    [0.00, 0.00, 0.00, 1.00]   # Desde Alta hospitalaria
])

# Crear DataFrame
df_T_inicial = pd.DataFrame(
    T_inicial,
    index=servicios,
    columns=servicios
)

print("MATRIZ DE TRANSICIÓN INICIAL")
print("=" * 70)
print(df_T_inicial)

print("\nVerificación: cada fila debe sumar 1")
print("-" * 70)
for i, serv in enumerate(servicios):
    suma = T_inicial[i, :].sum()
    status = "✓" if abs(suma - 1.0) < 1e-6 else "✗"
    print(f"{status} {serv:35}: suma = {suma:.3f}")

plt.figure(figsize=(10, 8))
sns.heatmap(
    T_inicial,
    annot=True,
    fmt='.2f',
    cmap='YlGnBu',
    xticklabels=servicios,
    yticklabels=servicios,
    cbar_kws={'label': 'Probabilidad de transición'},
    linewidths=0.5,
    linecolor='gray'
)

plt.title(
    'Matriz de Transición Inicial\nFlujo de Pacientes y Dietas Hospitalarias',
    fontsize=14,
    fontweight='bold',
    pad=20
)
plt.xlabel('Servicio destino', fontsize=12)
plt.ylabel('Servicio origen', fontsize=12)
plt.tight_layout()
plt.show()

print("\nLos valores más altos indican mayor probabilidad de tránsito entre servicios")

# Matriz de transición modificada (intervención hospitalaria)
T_intervencion = np.array([
    [0.15, 0.55, 0.20, 0.10],  # Desde Emergencia
    [0.05, 0.55, 0.25, 0.15],  # Desde Medicina Interna (más permanencia)
    [0.05, 0.15, 0.50, 0.30],  # Desde Cirugía (sin cambios)
    [0.00, 0.00, 0.00, 1.00]   # Desde Alta hospitalaria
])

df_T_intervencion = pd.DataFrame(
    T_intervencion,
    index=servicios,
    columns=servicios
)

print("\nMATRIZ DE TRANSICIÓN MODIFICADA (INTERVENCIÓN)")
print("=" * 70)
print(df_T_intervencion)

print("\nVerificación: cada fila debe sumar 1")
print("-" * 70)
for i, serv in enumerate(servicios):
    suma = T_intervencion[i, :].sum()
    status = "✓" if abs(suma - 1.0) < 1e-6 else "✗"
    print(f"{status} {serv:35}: suma = {suma:.3f}")

plt.figure(figsize=(10, 8))
sns.heatmap(
    T_intervencion,
    annot=True,
    fmt='.2f',
    cmap='YlOrRd',
    xticklabels=servicios,
    yticklabels=servicios,
    cbar_kws={'label': 'Probabilidad de transición'},
    linewidths=0.5,
    linecolor='gray'
)

plt.title(
    'Matriz de Transición con Intervención\nFortalecimiento de Medicina Interna',
    fontsize=14,
    fontweight='bold',
    pad=20
)
plt.xlabel('Servicio destino', fontsize=12)
plt.ylabel('Servicio origen', fontsize=12)
plt.tight_layout()
plt.show()

print("\nLa intervención incrementa la retención de pacientes en Medicina Interna")

# ============================================================
# CÁLCULO DE EIGENVALUES Y EIGENVECTORES
# MATRIZ MODIFICADA (INTERVENCIÓN HOSPITALARIA)
# ============================================================

# Cálculo de eigenvalues y eigenvectors
# Usamos la transpuesta para cadenas de Markov
eigenvalues, eigenvectors = linalg.eig(T_intervencion.T)

print("\nEIGENVALUES ENCONTRADOS")
print("=" * 70)

for i, val in enumerate(eigenvalues):
    if np.isreal(val):
        print(f"  λ_{i+1} = {val.real:8.5f}")
    else:
        print(f"  λ_{i+1} = {val.real:8.5f} + {val.imag:8.5f}i")

# Identificar eigenvalue dominante (|λ| máximo)
idx_dominante = np.argmax(np.abs(eigenvalues))
lambda_dominante = eigenvalues[idx_dominante]

print("\n" + "=" * 70)
print(f"EIGENVALUE DOMINANTE: λ_{idx_dominante+1} = {lambda_dominante.real:.6f}")

print("\nINTERPRETACIÓN:")
print("   • λ ≈ 1  → Existe un estado estacionario")
print("   • |λ| < 1 → El sistema converge al equilibrio")
print("   • La magnitud del segundo eigenvalue determina la velocidad de convergencia")
print("=" * 70)

# ============================================================
# VISUALIZACIÓN DE EIGENVALUES EN EL PLANO COMPLEJO
# ============================================================

plt.figure(figsize=(10, 8))

# Círculo unitario
theta = np.linspace(0, 2*np.pi, 200)
plt.plot(np.cos(theta), np.sin(theta), 'k--', alpha=0.4, linewidth=1.5)

# Ejes
plt.axhline(0, color='black', linewidth=0.7)
plt.axvline(0, color='black', linewidth=0.7)

# Graficar eigenvalues
for i, val in enumerate(eigenvalues):
    if i == idx_dominante:
        plt.scatter(val.real, val.imag,
                    s=300, marker='*',
                    color='red', edgecolor='black',
                    linewidth=2, zorder=3,
                    label='Eigenvalue dominante')
    else:
        plt.scatter(val.real, val.imag,
                    s=150, alpha=0.7,
                    edgecolor='black', linewidth=1.2)

    plt.annotate(f'λ_{i+1}',
                 (val.real, val.imag),
                 xytext=(8, 8),
                 textcoords='offset points',
                 fontsize=10, fontweight='bold')

plt.xlabel('Parte real', fontsize=12, fontweight='bold')
plt.ylabel('Parte imaginaria', fontsize=12, fontweight='bold')
plt.title('Eigenvalues de la Matriz de Transición Modificada',
          fontsize=14, fontweight='bold', pad=15)

plt.grid(True, alpha=0.3)
plt.axis('equal')
plt.legend()
plt.tight_layout()
plt.show()

# ============================================================
# DISTRIBUCIÓN ESTACIONARIA DEL SISTEMA HOSPITALARIO
# ============================================================

# Definición de servicios médicos del hospital
destinos = [
    'Emergencia',
    'Medicina Interna',
    'Cirugía',
    'Alta'
]

n_destinos = len(destinos)

# Extraer eigenvector asociado al eigenvalue dominante
v_dominante = eigenvectors[:, idx_dominante].real

# Normalizar para que sume 1 (distribución de probabilidad)
dist_estacionaria = v_dominante / v_dominante.sum()

print("\nDISTRIBUCIÓN ESTACIONARIA DE PACIENTES")
print("=" * 70)
print("\nDistribución de equilibrio (largo plazo):")
print("-" * 70)

for i, servicio in enumerate(destinos):
    porcentaje = dist_estacionaria[i] * 100
    barra = "█" * int(porcentaje / 2)
    print(f"{servicio:20} : {porcentaje:6.2f}% {barra}")

# Identificar servicio dominante
idx_hub = np.argmax(dist_estacionaria)

print("\n" + "=" * 70)
print(f"SERVICIO DOMINANTE DEL SISTEMA: {destinos[idx_hub]}")
print(f"   Concentra aproximadamente el {dist_estacionaria[idx_hub]*100:.2f}%")
print("=" * 70)

# ============================================================
# VISUALIZACIÓN DE LA DISTRIBUCIÓN ESTACIONARIA
# ============================================================

fig, ax = plt.subplots(figsize=(10, 6))

barras = ax.bar(destinos,
                dist_estacionaria * 100,
                alpha=0.75,
                edgecolor='black',
                linewidth=2)

ax.set_ylabel('Porcentaje de Pacientes (%)',
              fontsize=12, fontweight='bold')
ax.set_title('Distribución Estacionaria de Pacientes\n(Equilibrio a Largo Plazo)',
             fontsize=14, fontweight='bold', pad=15)

ax.grid(axis='y', alpha=0.3)
ax.set_ylim([0, max(dist_estacionaria * 100) * 1.2])

# Valores sobre las barras
for barra in barras:
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width()/2,
            altura,
            f'{altura:.1f}%',
            ha='center', va='bottom',
            fontsize=11, fontweight='bold')

plt.tight_layout()
plt.show()

# ============================================================
# INTERPRETACIÓN AUTOMÁTICA
# ============================================================

print("\nINTERPRETACIÓN DEL COMPORTAMIENTO A LARGO PLAZO:")
print("   • El estado 'Alta' actúa como un estado absorbente del sistema.")
print("   • A largo plazo, el 100% de los pacientes termina recibiendo el alta médica.")
print("   • La distribución estacionaria representa el destino final de los pacientes,")
print("     no la carga hospitalaria ni la ocupación de servicios.")
print("   • Para analizar impacto en Medicina Interna, es necesario estudiar")
print("     la evolución transitoria o redefinir 'Alta' como un estado no absorbente.")

