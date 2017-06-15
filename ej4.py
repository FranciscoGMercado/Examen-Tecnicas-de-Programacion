#ej4
import random
tupla = ("boca", 3, "river", 5)

def ganador():
    if tupla[1] < tupla[3]:
        print(tupla[0])
    else:
        print(tupla[2])
ganador()