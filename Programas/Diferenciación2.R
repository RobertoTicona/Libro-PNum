# Datos
epoca <- c(0,10,20,30,40,50)
loss  <- c(2.45, 1.82, 1.35, 1.08, 0.95, 0.89)
h <- 10

# Funciones para derivadas (usando h fijo = 10)
# Diferencia hacia adelante (para primer punto)
d_forward <- function(i) {
  (loss[i+1] - loss[i]) / h
}
# Diferencia hacia atrás (para último punto)
d_backward <- function(i) {
  (loss[i] - loss[i-1]) / h
}
# Diferencia centrada (para puntos interiores)
d_center <- function(i) {
  (loss[i+1] - loss[i-1]) / (2*h)
}
# Segunda derivada centrada
d2_center <- function(i) {
  (loss[i+1] - 2*loss[i] + loss[i-1]) / (h^2)
}

# Calcular derivadas en cada época
deriv <- numeric(length(loss))
for (i in seq_along(loss)) {
  if (i == 1) deriv[i] <- d_forward(i)
  else if (i == length(loss)) deriv[i] <- d_backward(i)
  else deriv[i] <- d_center(i)
}

# Calcular segunda derivada en puntos interiores
d2 <- rep(NA, length(loss))
for (i in 2:(length(loss)-1)) {
  d2[i] <- d2_center(i)
}

# Resultados pedidos:
cat("Derivadas (loss por época):\n")
print(data.frame(epoca=epoca, loss=loss, derivada=round(deriv, 5)))

cat("\nSegunda derivada (solo puntos interiores):\n")
print(data.frame(epoca=epoca, segunda_derivada=round(d2, 6)))

# 1) Tasa en época 20 (índice de época 3)
idx20 <- which(epoca == 20)
cat("\n1) f'(20) (centrada, h=10):", round(deriv[idx20], 5), " (loss/época)\n")

# 2) Segunda derivada en época 30
idx30 <- which(epoca == 30)
cat("2) f''(30):", round(d2[idx30], 6), " (loss/época^2)\n")

# Interpretación (impresa)
if (!is.na(d2[idx30])) {
  if (d2[idx30] > 0) {
    cat("   Interpretación: f''(30) > 0 → la magnitud de la pendiente se está reduciendo; la disminución del loss se está frenando (convergencia en curso).\n")
  } else if (d2[idx30] < 0) {
    cat("   Interpretación: f''(30) < 0 → la disminución se está acelerando.\n")
  } else {
    cat("   Interpretación: f''(30) ≈ 0 → curva cercana a lineal localmente.\n")
  }
}

# 3) ¿En qué época |f'| < 0.01 ?
idx_crit <- which(abs(deriv) < 0.01)
if (length(idx_crit) > 0) {
  cat("\n3) Épocas donde |f'| < 0.01:", epoca[idx_crit], "\n")
  cat("   Primera época que cumple el criterio:", epoca[min(idx_crit)], "\n")
} else {
  cat("\n3) No se alcanza |f'| < 0.01 en las épocas dadas.\n")
}

# 4) Estimación de loss en época 25 usando linearización en época 20:
t_target <- 25
t0 <- 20
f_t0 <- loss[which(epoca == t0)]
fprime_t0 <- deriv[which(epoca == t0)]
f25_est <- f_t0 + fprime_t0 * (t_target - t0)
cat("\n4) Estimación lineal (usando derivada en 20): f(25) ≈", round(f25_est, 4), "\n")

# Para comparación: interpolación lineal directa entre 20 y 30
f20 <- f_t0
f30 <- loss[which(epoca == 30)]
f25_lin_between <- f20 + (f30 - f20) * ( (t_target - 20) / (30 - 20) )
cat("   Interpolación lineal entre 20 y 30: f(25) ≈", round(f25_lin_between,4), "\n")