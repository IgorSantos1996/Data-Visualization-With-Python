import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]

titulo = "Gráfico de barras"
eixox = "Eixo x"
eixoy = "Eixo y"

# Titulo
plt.title(titulo)

# Eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.bar(x, y)
plt.show()