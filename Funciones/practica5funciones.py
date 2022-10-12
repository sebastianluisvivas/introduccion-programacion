# Practica 5 funciones

#Ejercicio 1
"""animales=["elefante","jirafa","mono"]
nuevoanimal=input("Ingrese un nuevo animal: ")
animales.append(nuevoanimal)
print(animales)"""


#Ejercicio 2:

"""

lista=[1,2,3,4,5] """












# Ejercicio 14

#Defnir una función llamada interseccion que tome dos listas sin repetidos y devuelva una nueva lista que contenga sólamente aquellos elementos que estén ambas listas.

def esta(lista,e):
    for elemento in lista:
        if elemento ==e:
            return True
    return False

def interseccion(lista1,lista2):
    nuevalista=[]

    for elemento in lista1:
        if esta(lista2,elemento):
            nuevalista.append(elemento)
    return nuevalista



# PP



lista1=[2,4,6,8,10]
lista2=[2,5,6,10,12]
print(interseccion(lista1,lista2))










