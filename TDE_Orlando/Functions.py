sumVet = lambda v1,v2: tuple(map(lambda x,y: x+y,v1,v2))
subVet = lambda v1,v2: tuple(map(lambda x,y: x-y,v1,v2))
##EscalarVet = lambda esc,vet: list(map((lambda x,y: x * y),esc,list(vet)))
eqReta = lambda p0,t0,u: tuple(sumVet(p0,EscalarVet(u,t0))) # p0 + u*t0

def EscalarVet(e0:float,v0:tuple):
    return tuple([e0 * i for i in v0])

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

#vet1 = [1,2,3]

#print(multEscalaVet(2,vet1))