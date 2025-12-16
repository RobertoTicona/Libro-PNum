# Datos
tiempo <- 0:7
temp <- c(20.1, 20.3, 20.8, 21.5, 22.6, 24.2, 26.1, 28.5)
h <- 1

# 1. Primera derivada (diferencias finitas)
vel <- numeric(length(temp))
for (i in seq_along(temp)) {
  if (i == 1) vel[i] <- (temp[i+1] - temp[i]) / h
  else if (i == length(temp)) vel[i] <- (temp[i] - temp[i-1]) / h
  else vel[i] <- (temp[i+1] - temp[i-1]) / (2*h)
}

# 2. Segunda derivada
acc <- rep(NA, length(temp))
for (i in 2:(length(temp)-1)) {
  acc[i] <- (temp[i+1] - 2*temp[i] + temp[i-1]) / (h^2)
}

# 3. Alertas (cuando velocidad > 0.8 °C/s)
alerta <- tiempo[vel > 0.8]

# 4. Normalización min-max
minmax <- function(x) (x - min(x, na.rm=TRUE)) / (max(x, na.rm=TRUE) - min(x, na.rm=TRUE))
vel_norm <- minmax(vel)
acc_norm <- minmax(acc)

# Mostrar resultados
df <- data.frame(tiempo, temp, vel, acc, vel_norm, acc_norm)
print(round(df, 3))

cat("\nMomentos con alerta (>0.8°C/s):", alerta, "segundos\n")