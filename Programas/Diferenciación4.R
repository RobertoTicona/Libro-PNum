# Datos
x <- c(-3, -2, -1, 0, 1, 2, 3)
sigma <- c(0.0474, 0.1192, 0.2689, 0.5000, 0.7311, 0.8808, 0.9526)
h <- 1

# Indices helper
idx <- function(val) which(x == val)

# 1) Derivada centrada para x = 0, -2, 2
deriv_centered <- function(xval) {
  i <- idx(xval)
  # asumiendo que xval tiene vecinos (x-h) y (x+h) disponibles
  (sigma[i + 1] - sigma[i - 1]) / (2 * h)
}

d0_num <- deriv_centered(0)
dminus2_num <- deriv_centered(-2)
d2_num <- deriv_centered(2)

# 2) Derivada analítica sigma*(1-sigma)
d_analytic <- sigma * (1 - sigma)
d0_ana <- d_analytic[idx(0)]
dminus2_ana <- d_analytic[idx(-2)]
d2_ana <- d_analytic[idx(2)]

# 3) Errores
abs_err_0 <- d0_num - d0_ana
rel_err_0 <- abs_err_0 / d0_ana * 100

abs_err_m2 <- dminus2_num - dminus2_ana
rel_err_m2 <- abs_err_m2 / dminus2_ana * 100

abs_err_2 <- d2_num - d2_ana
rel_err_2 <- abs_err_2 / d2_ana * 100

# Mostrar resultados
cat("Resultados (h = 1):\n\n")

cat("x = 0:\n")
cat("  derivada num (centrada) =", d0_num, "\n")
cat("  derivada analítica      =", d0_ana, "\n")
cat("  error absoluto =", abs_err_0, ", error relativo (%) =", rel_err_0, "\n\n")

cat("x = -2:\n")
cat("  derivada num (centrada) =", dminus2_num, "\n")
cat("  derivada analítica      =", dminus2_ana, "\n")
cat("  error absoluto =", abs_err_m2, ", error relativo (%) =", rel_err_m2, "\n\n")

cat("x = 2:\n")
cat("  derivada num (centrada) =", d2_num, "\n")
cat("  derivada analítica      =", d2_ana, "\n")
cat("  error absoluto =", abs_err_2, ", error relativo (%) =", rel_err_2, "\n\n")

# Tabla resumen
res <- data.frame(
  x = x,
  sigma = sigma,
  deriv_analitica = round(d_analytic, 8),
  deriv_centrada = c(NA, dminus2_num, NA, d0_num, NA, d2_num, NA)
)
cat("Tabla resumen:\n")
print(res)

# Recomendación sobre h (comentario)
cat("\nNota: si puedes evaluar sigma(x) analíticamente, usa h pequeño (p.ej. 1e-5) o mejor aún usa la derivada analítica.\n")