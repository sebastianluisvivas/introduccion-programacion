# s=0
# n=int(input("Cantidad de términos: "))
# for i in range (1,n+1):
#     s=s+1/i
# print("La serie para",n,"términos es:",s)



# n=int(input("Ingrese cantidad de términos: "))
# suma=0

# for i in range(1,n+1):
#     if(i%4==1 or i%4==2):
#         den=2
#     else:
#         den=4
#     suma=suma+i/den
# print("La serie para",n, "términos es",suma)



n=int(input("Ingrese la cantidad de términos: "))
suma=0
for i in range(1,n+1):
    if(i%2==0):
        suma=suma-1/i
    else:
        suma=suma+1/i
print("La suma de los",n,"primeros términos es",suma)
