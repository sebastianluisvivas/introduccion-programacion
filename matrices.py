# Ejercicio 25 práctica 5 - Listas

"""def controlV(ruta):
    patentes=darPatentes(ruta)
    for patente in patentes:
        veloc = controlVelocidad(patente)
        if veloc >100:
            if reincidente (patente):
            costo = costo *2
        else:
            costo = costo
            enviarMulta(patente,costo):

    #___ Hecho por la profe (bien)


# PowerPoint Matrices

    #____ Ejercicio 1

def esta (matriz,e):
    for lista in matriz:
        for elem in lista:
            if elem == e:
                return True
    return False """


matriz=[[16,10,10,8,2],[20,10,8,6],[6,6,6,4,8,30],[8,4,2,4],[10,6,8,14,12],[12,12,18,10,6]]


def cuantas (e,matriz):
    lista = []
    lista.append()
    contador=0
    for lista in matriz:
        for elemento in lista:
            if elemento == e:
                contador=contador+1
        lista.append(contador)
        contador=0
    return lista
print(cuantas(matriz,6))






