import matplotlib.pyplot as plt
x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]
z = [200, 35, 400, 3300, 33] 
titulo = "Scatterplot: gráfico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.plot(x, y, color = "#000000", linestyle="--")
plt.scatter(x, y, label = "Meus pontos", color = "g", marker = "h", s = 200)

plt.legend()

#plt.show()
plt.savefig("figura1.png", dpi = "72")
