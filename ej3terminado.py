import random
def ej3():
    matriz = []
    for y in range(6):
        linea = []
        for x in range(6):
            numeros = random.randint(1, 55)
            linea.append(numeros)
        matriz.append(linea)
    matriz[0][0] = 0
    matriz[1][1] = 0
    matriz[2][2] = 0
    matriz[3][3] = 0
    matriz[4][4] = 0
    matriz[5][5] = 0

    print(matriz[0])
    print(matriz[1])
    print(matriz[2])
    print(matriz[3])
    print(matriz[4])
    print(matriz[5])
print(ej3())