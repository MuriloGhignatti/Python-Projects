def Soma(vet1:tuple,vet2:tuple):
    return [vet1[i] + vet2[i] for i in range(vet2.__len__()) if vet1.__len__() == vet2.__len__()]
def Subtração(vet1:tuple,vet2:tuple):
    return [vet1[i] - vet2[i] for i in range(vet2.__len__()) if vet1.__len__() == vet2.__len__()]
def Multiplicação(vet1:tuple,escalar:float):
    return [escalar * i for i in vet1]
def Reta_Ponto(p0:tuple,t0:tuple,u:float):
    return Soma(p0,Multiplicação(t0,u))
def Reta_DPonto(p0:tuple,p1:tuple,u:float):
    return Soma(p0,Multiplicação(Subtração(p1,p0),u))

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