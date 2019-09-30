def SomaVet(v0:tuple,v1:tuple):
    return tuple([v0[i] + v1[i] for i in range(v0.__len__()) if v0.__len__() == v1.__len__()])

def SubVet(v0:tuple,v1:tuple):
    return tuple([v0[i] - v1[i] for i in range(v0.__len__()) if v0.__len__() == v1.__len__()])

def EscalarVet(e0:float,v0:tuple):
    return tuple([e0 * i for i in v0])

def Reta(p0:tuple,u:float,t0:tuple): #p0 + u * t (Onde p0[Tupla] u[Escalar] t[Tupla])
    return tuple(SomaVet(p0,EscalarVet(u,t0)))

def toReta(p0:tuple,u:float,p1:tuple): #p0 + u(p1 - p0) (Onde p0[Tupla] u[Escalar] p1[Tupla])
    return tuple(SomaVet(p0,EscalarVet(u,SubVet(p1,p0))))

def multiVet(MatrizA,MatrizB):
    Resultante = []
    for Linha in range(MatrizA.__len__()):
        soma = 0
        for Coluna in range(MatrizA[0].__len__()):
            soma = MatrizA[Linha][Coluna] * MatrizB[Linha][Coluna]
            Resultante.append(soma)
    return soma

print(multiVet([[1,2],[2,1]],[[2,2],[3,3]]))