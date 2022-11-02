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

