"""def divprop (a):
    divisoresPropios=[]
    for i in range (1,a):
        if (a%i==0):
            divisoresPropios.append(i)
    print(divisoresPropios)



a=int(input("Ingrese un numero: "))
print("Los divisores propios de",a,"son:")
divprop(a)  """



# Hacer una función que recibe una lista y un entero e indique si el entero está en la lista.
"""
def esta(lista,e):
    for elemento in lista:
        if elemento == e:
            return True
    return False


## PP

lista1=[1,7,9,5]
elem=7
if esta(lista1,elem):
    print(elem,"está en la lista")
else:
    print(elem,"No está en la lista")  """


# Hacer una función que dado un entero y una lista de enteros indique cuantas veces aparece el entero en la lista.

"""def cuantas (listaenteros):
    contador=0
    for elemento in listaenteros:
        if elemento == entero:
            contador=contador+1
    return contador


## PP

listaenteros=[1,5,6,7,7,10,6]
entero=6
print(cuantas) """



#Hacer una función que reciba una lista de enteros y devuelva el máximo.

"""def masGrande(lista):
    max=lista[0]
    for elemento in lista:
        if elemento > max:
            max=elemento
    return max


## PP

lista1=[1,7,9,5]
print(masGrande(lista1),"es el más grande de la lista")  """


# Hacer una función que reciba una lista y devuelva otra solo con los elementos sin repeticiones.

#________Hecha por mi, mal

"""def elemsinrep (lista):
    sinrepeticiones=[]
    for elemento in lista:
        if elemento != elemento:
            sinrepeticiones.append(elemento)



# PP

lista=[1,2,3,3,5,5,7,10,10]
sinrepeticiones=[]
print(sinrepeticiones(),"Son los elemento sin repeticiones") """



# ______hecho por la profe

def esta(lista,e):
    for elemento in lista:
        if elemento==e:
            return True
    return False


def sinRepetidos(lista):
    nueval=[]
    for elem in lista:
        if not esta(nueval,elem):
            nueval.append(elem)
    return nueval

## PP

lista=[1,1,2,2]
print(sinRepetidos(lista))