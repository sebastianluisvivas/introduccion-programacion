
#          \ ____________________________________    Ejercicio 1    ____________________________________ |



# a) Hacer un programa que muestre, mediante un ciclo, los primeros 5 números naturales (1, 2, 3, 4 y 5).
# b) Hacer un programa que permita al usuario elegir un número n y luego muestre los primeros n números naturales (1, 2, · · · , n).s


#                         (___________          A           ___________ )

# print("Este programa emitirá los primeros 5 números naturales:")
# for i in range(1,6):
#     print(i)


#                         (___________          B           ___________ )


# n=int(input("Elija un número: "))
# for i in range(1,n):
#     print(i)



#          \ ____________________________________    Ejercicio 2    ____________________________________ |

# a) Hacer un programa que muestre, mediante un ciclo, los números desde el 4 hasta el 7 (4, 5, 6 y 7).

# b) Hacer un programa que permita al usuario elegir un número m y un n y luego muestre todos los naturales entre m y n
# (m, m + 1, m + 2, · · · , n − 1, n). ¿Qué pasa si n es menor que m?


#                         (___________          A           ___________ )
# a=3
# num=4
# for i in range(3,7):
#     a=a+1
#     print(a)

#                         (___________          B           ___________ )

# m=int(input("Ingrese un número: "))
# n=int(input("Ingrese un número: "))
# for i in range (m,n+1):
#     print(i)




#          \ ____________________________________    Ejercicio 3    ____________________________________ |

#                         (___________          A           ___________ )

# a) Hacer un programa que muestre, mediante un ciclo, los 5 números naturales que le siguen al 10 (11, 12, · · · , 15).

# n=10
# for i in range(n+1,16):
#     print(i)


#                         (___________          B           ___________ )

#b) Hacer un programa que permita al usuario elegir un número n y luego muestre
#  los 5 números naturales que le siguen a n (n + 1, n + 2, · · · , n + 5).


# n=int(input("Ingrese un número: "))
# for i in range(n+1,n+6):
#     print(i)



#                         (___________          C           ___________ )

#c) Hacer un programa que permita al usuario elegir un número n y un número c, y
# luego muestre los c números naturales que le siguen a n (n + 1, n + 2, · · · , n + c)

# n=int(input("Ingrese un primer número: "))
# c=int(input("Ingrese un segundo número: "))
# for i in range(n+1,c+1):
#     print(i)


#          \ ____________________________________    Ejercicio 4    ____________________________________ |


#                         (___________          A           ___________ )

# a) Hacer un programa que muestre, mediante un ciclo, los números desde el 5 hasta el 11 salteando de a 2 elementos (5, 7, 9 y 11)

"""n=5
for i in range(n,12,2):
    n=n+2
    print(i)"""


#                         (___________          B           ___________ )

# b) Hacer un programa que permita al usuario elegir un número m y un n y luego muestre todos los naturales entre m y n, pero salteando de a 3.
#  Por ejemplo, si el usuario ingresara un n igual a 2 y un m igual a 14, el programa deberá mostrar 2, 5, 8, 11, 14.
"""m=int(input("Ingrese un primer número: "))
n=int(input("Ingrese un segundo número: "))
for i in range(m,n+1,3):
    print(i)"""
#                         (___________          C           ___________ )

# c) Hacer un programa que permita al usuario elegir un número n, un m y un p y luego muestre todos los naturales entre m y n,
# pero salteando de a p números. Por ejemplo, si el usuario ingresara un n igual a 2 y un m igual a 14, y un p igual a 4,
# el programa deberá mostrar 2, 6, 10, 14.
"""m=int(input("Ingrese un primer número: "))
n=int(input("Ingrese un segundo número: "))
p=int(input("Ingrese la cantidad de números a saltear:  "))
for i in range (m,n+1,p):
    print(i)"""





#          \ ____________________________________    Ejercicio 5    ____________________________________ |


#                         (___________          A           ___________ )

# a) Hacer un programa que muestre, mediante un ciclo, los números desde el 8 hasta el 3 (8, 7, 6, 5, 4, 3)
"""n=8
for i in range(8,2,-1):
    print(i)"""




#          \ ____________________________________    Ejercicio 6    ____________________________________ |


#a) Hacer un programa que muestre, mediante un ciclo, los números desde el 15 hasta el 6 pero salteando de a tres (15, 12, 9, 6).

"""n=15
for i in range(15,5,-3):
    print(i)""""






#          \ ____________________________________    Ejercicio 8    ____________________________________ |

# ¿Es verdad que las únicas soluciones enteras de x(x+2)(x+3) = 1 son x = 1 x = −2 y x = −3?. Hacer un programa que encuentre todas las soluciones enteras de 1 0 2 cifras tanto negativas como positivas








#          \ ____________________________________    Ejercicio 9    ____________________________________ |

"""Hacer un programa que solicite un número x, en caso de ser par realiza x/2 y en caso contrario 3x + 1 y repite el procedimiento hasta obtener el número 1.
El programa debe indicar cuantas veces se tuvo que repetir el procedimiento.
Por ejemplo, si se ingresa el número 10 el programa devuelve 6, porque 10 es par entonces lo divide por 2 y da 5, como es impar lo multiplica por 3 y le suma 1 obteniendo 16. Luego da 8, 4, 2 y 1.
Otro ejemplo: si se ingresa 27 debe devolver 111."""








