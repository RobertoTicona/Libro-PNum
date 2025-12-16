# Código R: cálculo automático de derivadas y decisiones
gasto <- c(0, 5, 10, 15, 20, 25)   # en $k
conv  <- c(2.1, 3.8, 5.2, 6.1, 6.7, 7.0)  # en %
h <- 5  # en $k

# 1) Derivadas (ROI marginal) - forward/back/centered
deriv <- numeric(length(conv))
for (i in seq_along(conv)) {
  if (i == 1) {
    deriv[i] <- (conv[i+1] - conv[i]) / h    # forward
  } else if (i == length(conv)) {
    deriv[i] <- (conv[i] - conv[i-1]) / h    # backward
  } else {
    deriv[i] <- (conv[i+1] - conv[i-1]) / (2*h)  # centered
  }
}

# 2) Segunda derivada centrada (interiores)
d2 <- rep(NA, length(conv))
for (i in 2:(length(conv)-1)) {
  d2[i] <- (conv[i+1] - 2*conv[i] + conv[i-1]) / (h^2)
}

# 3) ¿Dónde f'(x) > 0.2 % por $1k?
idx_gt_02 <- which(deriv > 0.2)
gasto_gt_02 <- gasto[idx_gt_02]

# punto aproximado donde f'(x)=0.2 (lineal entre 10 y 15 si desea precisión)
d10 <- deriv[which(gasto==10)]
d15 <- deriv[which(gasto==15)]
if (d10 != d15) {
  frac <- (d10 - 0.2) / (d10 - d15)
  x_threshold <- 10 + frac * (15 - 10)  # en $k
} else {
  x_threshold <- NA
}

# Impresión de resultados
cat("Gasto ($k)  :", gasto, "\n")
cat("Conversion % :", conv, "\n\n")
cat("ROI marginal f' (% per $1k):\n")
print(round(deriv, 4))

cat("\nSegunda derivada (interiores) f'' (% per ($1k)^2):\n")
print(round(d2, 5))

cat("\nPuntos donde f' > 0.2 (% per $1k):", gasto_gt_02, "\n")
cat("Umbral f'(x)=0.2 ocurre aproximadamente en gasto = ", round(x_threshold, 3), " $k\n\n")

# Recomendación basada en derivadas
cat("Interpretación:\n")
cat("- f'(25) =", round(deriv[length(deriv)],4), "%/ $1k  (marginal positivo pero bajo)\n")
cat("- f'' en interiores (ej. f''(15) =", round(d2[which(gasto==15)],5), ") indica rendimientos decrecientes\n")
cat("--> Matemáticamente no conviene aumentar demasiado el gasto más allá de 25k si la meta es obtener conversion % por dolar adicional.\n")