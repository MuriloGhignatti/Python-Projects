from functools import reduce

matrizes = [[10,9.7,9.8,10,8.7],
            [8.6,5.8,7.3,9.1,9.2],
            [4.0,7.0,5.0,4.7,3.2],
            [9.2,5.3,8.9,8.7,6.5]]

coluna = lambda matriz,coluna: [linha[coluna] for linha in matriz]

maximo = lambda matriz,linha: reduce(lambda x, y: x if x > y else y, matriz[linha])

minimo = lambda matriz,linha: reduce(lambda x, y: y if x > y else x, matriz[linha])

somaLinha = lambda matriz,linha: reduce((lambda x, y: x + y), matriz[linha])

somaColuna = lambda matriz,coluna: reduce(lambda x,y: x+y,[linha[coluna] for linha in matriz])

mediaLinha = lambda matriz,linha: somaLinha(matriz,linha)/matriz[linha].__len__()

mediaColuna = lambda matriz,col: somaColuna(matriz,col)/coluna(matriz,col).__len__()

#print(somaColuna(matrizes,3))

print(mediaColuna(matrizes,2))