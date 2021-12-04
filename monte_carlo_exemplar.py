import random

def f(x):
    return 3 * x + 2

def g(x):
    return 2 * x + 2

def calculo(numPontos, poluidoA, poluidoB, areaCompleta):
    pontosAreaPoluida = 0
    pontosAreaCompleta = 0
    listaXi = []
    listaYi = []
    for v in range(numPontos):
        listaXi.append(random.uniform(0, m))
        listaYi.append(random.uniform(0, n))
    for i in range(numPontos):
        if poluidoA <= listaXi[i] <= poluidoB:
            if g(listaXi[i]) <= listaYi[i] <= f(listaYi[i]):
                pontosAreaPoluida += 1
                pontosAreaCompleta += 1
            else:
                pontosAreaCompleta += 1
        else:
            pontosAreaCompleta += 1

    areaPoluida = (pontosAreaPoluida / pontosAreaCompleta) * areaCompleta
    return areaPoluida


poluidoA = float(input('Menor valor de x do rio poluído: '))
poluidoB = float(input('Maior valor de x do rio poluído: '))
m = float(input('Maior valor de x da área completa: '))
n = float(input('Maior valor de y da área completa: '))
areaCompleta = m * n

print(calculo(100, poluidoA, poluidoB, areaCompleta))
print(calculo(500, poluidoA, poluidoB, areaCompleta))
print(calculo(1000, poluidoA, poluidoB, areaCompleta))
print(calculo(5000, poluidoA, poluidoB, areaCompleta))
print(calculo(10000, poluidoA, poluidoB, areaCompleta))
print(calculo(50000, poluidoA, poluidoB, areaCompleta))
print(calculo(100000, poluidoA, poluidoB, areaCompleta))
print(calculo(500000, poluidoA, poluidoB, areaCompleta))
print(calculo(1000000, poluidoA, poluidoB, areaCompleta))
print(calculo(10000000, poluidoA, poluidoB, areaCompleta))
