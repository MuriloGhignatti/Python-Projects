from matplotlib import pyplot as plt

def SomaVet(v0:tuple,v1:tuple):
    return tuple([v0[i] + v1[i] for i in range(v0.__len__()) if v0.__len__() == v1.__len__()])

def SubVet(v0:tuple,v1:tuple):
    return tuple([v0[i] - v1[i] for i in range(v0.__len__()) if v0.__len__() == v1.__len__()])

def EscalarVet(e0:float,v0:tuple):
    return tuple([e0 * i for i in v0])

def Reta(p0:tuple,u:float,t0:tuple): #p0 + u * t (Onde p0[Tupla] u[Escalar] t[Tupla])
    return tuple(SomaVet(p0,EscalarVet(u,t0)))

def RetaX(lista):
    X = []
    for i in range(lista.__len__()):
        for j in range(lista[0].__len__()):
            if j == 0:
                X.append(lista[i][0])
    return X
def RetaY(lista):
    Y = []
    for i in range(lista.__len__()):
        for j in range(lista[0].__len__()):
            if j == 1:
                Y.append(lista[i][1])
    return Y

VetorParalelo = [Reta((0.8,2),u,(-1,1)) for u in range(-5,14)]

A = [Reta((-1,2),u,(1,1)) for u in range(-5,10)]
B =[Reta((1,3),u,(-1,1)) for u in range(10)]

X = RetaX(VetorParalelo)
Y = RetaY(VetorParalelo)

xa = RetaX(A)
ya = RetaY(A)

xb = RetaX(B)
yb = RetaY(B)

plt.plot(X,Y,color="red") #Reta Paralela a B e que passa na extremidade do vetor A
plt.plot(xa,ya,color="blue") #Vetor A
plt.plot(xb,yb,color="green") #Vetor B
plt.show()

def Lapiz(ponto:tuple):
    Points = lambda x,sum,p1:[Reta(SomaVet(ponto,sum),u,p1) for u in range(x)]
#Lado Esquerdo
    plt.plot(RetaX(Points(10,(0,0),(0,2))),RetaY(Points(10,(0,0),(0,2))))
    #Lado Direito
    plt.plot(RetaX(Points(10,(1,1),(0, 2))), RetaY(Points(10,(0,0),(0, 2))))
#Cima
    plt.plot(RetaX(Points(10,(1, 4), (-0.11, 1))), RetaY(Points(10,(3, 18), (1, 0))))
#Ponta Esquerda
    plt.plot(RetaX(Points(6,(0.55, 1), (-0.11, 1))), RetaY(Points(6,(0, -5), (0, 1))))
#Ponta Direita
    plt.plot(RetaX(Points(6, (0.44, 2), (0.11, 1))), RetaY(Points(6, (0, -5), (0, 1))))


def LapizReta(ponto:tuple):
    Reta_Ponto = [Reta(ponto,u,(1,1)) for u in range(10)]
    plt.plot(RetaX(Reta_Ponto),RetaY(Reta_Ponto))
    for i in range(4):
        Lapiz((Reta_Ponto[i][0], Reta_Ponto[i][1]))
    plt.show()

#Lapiz((0,0))
#plt.show()
#LapizReta((100,200))