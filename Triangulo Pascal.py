from math import *
def gerarListaNula(n):
    return [0 for c in range(n)]
def gerarMatrizNula(c,l):
    return [gerarListaNula(c) for i in range(l)]
def CombS(n,p):
    return factorial(n) / (factorial(p) * factorial((n - p)))
def tri(l):
    Li = l+1
    c = l+1
    M = gerarMatrizNula(c,Li)
    for o in range(Li):
        for i in range(c):
            if o == 0 and i == 0:
                M[o][i] = CombS(o,o - i)
            elif o != 0 and i <= o:
                M[o][i] = CombS(o,o - i)
    return M
def zero(x):
    for i in x:
        for c in range(i.__len__()):
            for j in i:
                if j == 0:
                    i.remove(0)
    return x
for c in zero(tri(15)): print(c)
