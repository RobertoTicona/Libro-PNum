# Datos
dias <- c("Lun","Mar","Mié","Jue","Vie","Sáb","Dom")
ventas <- c(45, 52, 61, 58, 73, 89, 95)  # en $k
h <- 1

# 1) Primera derivada: adelante en primer punto, atrás en último, centrada en interiores
deriv <- numeric(length(ventas))
for (i in seq_along(ventas)) {
  if (i == 1) {
    deriv[i] <- (ventas[i+1] - ventas[i]) / h
  } else if (i == length(ventas)) {
    deriv[i] <- (ventas[i] - ventas[i-1]) / h
  } else {
    deriv[i] <- (ventas[i+1] - ventas[i-1]) / (2*h)
  }
}

# 2) Segunda derivada (centrada) en puntos interiores
d2 <- rep(NA, length(ventas))
for (i in 2:(length(ventas)-1)) {
  d2[i] <- (ventas[i+1] - 2*ventas[i] + ventas[i-1]) / (h^2)
}

# Identificar día con mayor aceleración positiva
idx_max_acc <- which.max(d2)  # returns first max (NA treated as -Inf)
# but ensure it's interior (non-NA)
if (is.na(d2[idx_max_acc]) || length(idx_max_acc) == 0) {
  dia_max_acc <- NA
  max_acc <- NA
} else {
  dia_max_acc <- dias[idx_max_acc]
  max_acc <- d2[idx_max_acc]
}

# 3) Magnitud de la caída el jueves (drop Mié -> Jue)
drop_jue <- ventas[4] - ventas[3]  # index 4 = Jue, 3 = Mié

# 4) Extrapolación lineal para Lunes siguiente usando derivada en Domingo
f_dom <- ventas[length(ventas)]
fprime_dom <- deriv[length(ventas)]
f_lun_sig <- f_dom + fprime_dom * 1

# Mostrar resultados
cat("Primera derivada (ventas $k/día) por día:\n")
print(data.frame(dia=dias, ventas=ventas, derivada=deriv))

cat("\nSegunda derivada (ventas $k/día^2) en puntos interiores:\n")
print(data.frame(dia=dias, segunda_derivada=d2))

cat("\nDía con mayor aceleración positiva:\n")
cat("  ", dia_max_acc, "con f'' =", max_acc, "\n")

cat("\nCaída en ventas Mié -> Jue: ", drop_jue, " $k (si es negativo, es caída)\n")

cat("\nProyección lunes siguiente (usando derivada en domingo):\n")
cat("  Ventas domingo =", f_dom, " $k\n")
cat("  Tasa domingo =", fprime_dom, " $k/día\n")
cat("  Estimación lunes siguiente =", f_lun_sig, " $k\n")