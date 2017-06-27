import random
def ej3():
    L = []
    J = []
    M = []
    matriz = [[L], [J], [M]]
    N = int(4)
    valor = int(2)
    for i in range(N):
        L.append(random.randint(0,100))
    for i in range(N):
        J.append(random.randint(0,100))
    for i in range(N):
        M.append(random.randint(0,100))
    print(matriz[0][0:])
    print(matriz[1][0:])
    print(matriz[2][0:])
print(ej3())