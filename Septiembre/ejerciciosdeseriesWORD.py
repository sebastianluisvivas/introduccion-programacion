# # El word contiene 3 páginas.   Título del .doc: "Ejercicios de Series"

# #                                            \ ____________________ Ejercicio 1 ____________________ / 

# #Escribir un programa que calcule e imprima el resultado de la siguiente serie, teniendo en cuenta que n es un número introducido por teclado. 

# # Pedir cantidad de términos
# n=int(input("Ingrese la cantidad de términos: "))
# # Inicio variable contador para sumar los términos de la serie. Arranca en 0 ya que no tengo nada todavía
# suma=0
# # Identifico/busco un término general fácil, arriba siempre es 1 y abajo puede ser un i que crece en +1
# # Inicio ciclo for desde el 1 y con su crecimiento
# for i in range (1,n+1):
#     # La serie tiene signos + y -, analizo cuando suma o resta con respecto a la variable i.
#     # i par = resta        i impar = suma
#     if (i%2==0):
#         # Acumulo en la variable "suma" los términos de la serie cuando i es par
#         suma=suma-1/i
#     else:
#         # Ahora para impar
#         suma=suma+1/i
# # Al salir del for, muestro el resultado que está en suma
# print("La suma de los",n,"primeros términos es",suma)






# #                                          \ ____________________ Ejercicio 11 ____________________ / 

# Escribir un programa que dado un n ---determine cuantos términos--- se deben sumar antes de llegar a n. 

#En este caso se debe utilizar un while

# Pido la cantidad de términos que será n e inicio el contador
n=int(input("Ingrese la cantidad de términos"))
suma=0

# Como estoy usando while, a la variable i la debo inicializar en i
i=1

while (suma<=n):
    suma=suma+1/i
    # Incremento la variable i en 1
    i=i+1
# Al salir del while imprimo la cantidad de términos que se necesitan antes de llegar a n
print("Los términos que se necesitan antes de llegar a n son",i-1)