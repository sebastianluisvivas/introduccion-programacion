# Ejercicio 25 práctica 5 - Listas

def controlV(ruta):
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
    return False