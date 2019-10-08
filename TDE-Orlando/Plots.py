from matplotlib import pyplot  as plt
from Funcoes_Vetorias import Reta_DPonto,RetaX,RetaY
import numpy as np
import Bezier


pontos = [Reta_DPonto((0.75,1),(1.75,1),u) for u in range(2)]

fig, ax = plt.subplots()

Bezier.Bezier((0.75,1),(0.65,1.15),(0.75,1.50))
Roda_Esquerda = plt.Circle((0.75,0.96),0.1)
Roda_Direita = plt.Circle((1.75,0.96),0.1)
ax.add_artist(Roda_Esquerda)
ax.add_artist(Roda_Direita)

X = RetaX(pontos)
Y = RetaY(pontos)

plt.plot(X,Y)

plt.xlim(0,2)
plt.ylim(0,2)
plt.show()