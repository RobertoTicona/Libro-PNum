# Código R para calcular automáticamente lo anterior

# Datos
hora <- 0:7
latencia <- c(120, 125, 128, 135, 280, 290, 275, 155)
h <- 1

# 1) Primera derivada: adelante, centrada, atrás
fprime <- numeric(length(latencia))
for (i in seq_along(latencia)) {
  if (i == 1) {
    fprime[i] <- (latencia[i+1] - latencia[i]) / h          # forward
  } else if (i == length(latencia)) {
    fprime[i] <- (latencia[i] - latencia[i-1]) / h          # backward
  } else {
    fprime[i] <- (latencia[i+1] - latencia[i-1]) / (2*h)    # centered
  }
}

# 2) Segunda derivada centrada (puntos interiores)
f2 <- rep(NA, length(latencia))
for (i in 2:(length(latencia)-1)) {
  f2[i] <- (latencia[i+1] - 2*latencia[i] + latencia[i-1]) / (h^2)
}

# 3) Magnitud salto 3->4
salto_3_4 <- latencia[5] - latencia[4]  # indices: hora 4 is index 5, hora 3 is index 4

# 4) Tasas de recuperación (a partir de la hora 6)
idx6 <- which(hora == 6)
tasa_recuperacion_cent <- fprime[idx6]
# derivada entre 6->7 (forward from 6 or backward at 7)
tasa_6_7 <- (latencia[8] - latencia[7]) / h  # index 8=hora7, 7=hora6

# 5) Detección de anomalías: |f'| > 50 ms/h
umbral <- 50
anomalias_idx <- which(abs(fprime) > umbral)
anomalias_horas <- hora[anomalias_idx]

# Imprimir resultados
cat("Primera derivada f' (ms/h) por hora:\n")
print(data.frame(hora=hora, latencia=latencia, fprime=round(fprime,4)))

cat("\nSegunda derivada f'' (ms/h^2) en puntos interiores:\n")
print(data.frame(hora=hora, f2=f2))

cat("\nSalto brusco 3->4 (ms):", salto_3_4, "\n")

cat("\nTasa de recuperación (hora 6, centrada):", tasa_recuperacion_cent, "ms/h\n")
cat("Tasa entre 6->7:", tasa_6_7, "ms/h\n")

if (length(anomalias_idx) > 0) {
  cat("\nAnomalías detectadas (|f'| >", umbral, "ms/h) en horas:", anomalias_horas, "\n")
} else {
  cat("\nNo se detectaron anomalías con el umbral dado.\n")
}