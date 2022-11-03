# Practica 5 de LISTAS - 
# https://virtual.grado.ungs.edu.ar/moodle/pluginfile.php?file=%2F42386%2Fmod_resource%2Fcontent%2F12%2F5-Listas.pdf 


# __________   Recorrer LISTAS con ciclo for y while  ______________________


# -- Recorrer lista por ÍNDICE
"""animales = ["gato", "perro", "raton"]
i = 0
while (i < len(animales)):
    print(animales[i])
    i = i + 1 """""


""" for i in range(len(animales)):
    print (animales[i]) """""

# -- Recorrer lista por ELEMENTO
# La variable elemento cambia en cada iteracón sin importar la posición que ocupa c/elemento en la lista

"""for elemento in animales:
    print (elemento) """""
    

# _______________________ EJERCICIOS _________________

#Hacer un programa que guarde la siguiente lista en una variable: ["elefante", "jirafa","mono"], 
# luego pida el nombre de otro animal, lo agregue a la lista e imprima en pantalla el cuarto animal de la lista
"""""
animales = ["elefante","jirafa","mono"]
pedir_animal = input("Ingrese un animal: ")
animales.append(pedir_animal)
print(animales)
print("El cuarto animal es:", pedir_animal)
"""


# _____________       3      __________________


#Ejercicio 3 F
#Definir una función llamada divisores que tome un entero y devuelva la lista de divisores de ese entero.
"""""
def divisores (entero):           # entero es el parametro
    list_diventeros = []
    contador = 0
    for divisor in range(1,entero+1):
        if (entero % divisor == 0):
            #print(divisor, "es divisor")
            contador = contador+1
            list_diventeros.append(divisor)
    return(list_diventeros)
"PP"    

entero = int(input("Ingrese un número: "))

print("Los divisores de",entero, "son: ",divisores(entero))               # entero es argumento 
"""""




# _____________       4      __________________
#Ejercicio 4 F

#Definir una función llamada laMasCorta que tome dos listas y devuelva la que tenga menos elementos. 
# Si tienen igual cantidad, deberá devolver la primera.

def laMasCorta(lista1,lista2):
    if len(lista1) == len(lista2):
        return("Ambas listas son iguales, se devuelve la primera: ",lista1)
    else:
        if len(lista1) < len(lista2):
            return("La lista más corta es la primera",lista1)
        else:
            return("La lista más corta es la segunda",lista2)


# PP
lista1=[10,15,10,18,17,19,20,22,13,58,94,78,46,15,48,8,79,45,13]
lista2=[12,19,15,46,48,78,45,81,99,100,15,45,64,84,79,51,644,48,78]
print(laMasCorta(lista1,lista2))