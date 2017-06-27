ruta = str(input('Ingrese una ruta de archivo valida: '))
extencion = str(input('Ingrese una extencion de archivo valida: '))
def ej3():
    if(extencion in ruta):
        print('es una ruta valida.')
    else:
        print('No es una ruta valida para esa extencion!!!')
        print(ruta)
ej3()
