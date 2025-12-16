# Datos
mes <- 1:7
usuarios <- c(10, 15, 23, 34, 48, 65, 85)
h <- 1

# 1. Derivadas (tasa de crecimiento)
# Diferencia adelante, atrás y centrada
dif_adelante <- (usuarios[2] - usuarios[1]) / h
dif_atras <- (usuarios[7] - usuarios[6]) / h
dif_centrada <- (usuarios[5] - usuarios[3]) / (2*h)

cat("Tasa mes 1 (adelante):", dif_adelante, "miles/mes\n")
cat("Tasa mes 4 (centrada):", dif_centrada, "miles/mes\n")
cat("Tasa mes 7 (atrás):", dif_atras, "miles/mes\n")

# 2. Segunda derivada (aceleración) en puntos interiores
f2 <- numeric(length(usuarios))
for (i in 2:(length(usuarios)-1)) {
  f2[i] <- (usuarios[i+1] - 2*usuarios[i] + usuarios[i-1]) / (h^2)
}
f2

cat("\nSegunda derivada (aceleración) por mes:\n")
print(data.frame(mes=mes, aceleracion=f2))

# 3. Interpretación
if (all(f2[2:6] > 0)) {
  cat("\nLa aceleración es positiva → crecimiento acelerado.\n")
} else if (all(f2[2:6] < 0)) {
  cat("\nLa aceleración es negativa → crecimiento desacelerado.\n")
} else {
  cat("\nLa aceleración varía → crecimiento irregular.\n")
}