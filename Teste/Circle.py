from matplotlib import pyplot as plt
from Functions import Reta
from numpy import arange

def Circle(var):
    X = []
    Y = []
    lista = [Reta((2,3),u,(1,1)) for u in range(-2,3)]

    circle1 = plt.Circle(Reta((2,3),var,(1,1)), 0.2, color='r')
    fig, ax = plt.subplots()
    ax.add_artist(circle1)

    for i in range(lista.__len__()):
        for j in range(lista[0].__len__()):
         if j == 0:
              X.append(lista[i][0])
         if j == 1:
              Y.append(lista[i][1])

    plt.plot(X,Y,color='orange')
    plt.show()

for i in arange(-2.0,3.0,0.1):
    Circle(i)