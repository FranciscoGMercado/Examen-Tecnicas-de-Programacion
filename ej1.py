#print("pruevas varias")
lista2 = [2, 5, 9, 46, 3]
lista1 = [18, lista2]
lista3 = []
n = lista1[0]
print(lista1)
def ej1():
    for x in lista2:
        if n % x == 0:
            lista3.append(x)
            #print(lista3)
ej1()
print(lista3)