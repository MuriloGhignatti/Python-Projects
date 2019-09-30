from matplotlib import pyplot as plt
from Functions import Reta
from Functions import toReta

#Construir o gráfico da reta que passa pelo ponto p0(2,3) e tem direção v(1,1)

#(x,y) = (2,3) + u(1,1)

lista = [Reta((2,3),u,(1,1)) for u in range(-2,3)]

X = []
Y = []

for i in range(lista.__len__()):
    for j in range(lista[0].__len__()):
        if j == 0:
            X.append(lista[i][0])
        if j == 1:
            Y.append(lista[i][1])

plt.plot(X,Y)
plt.show()

print(f"{X} \n {Y}")