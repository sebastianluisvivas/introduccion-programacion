print("Este programa calcula ")

n=int(input("Ingrese un número natural: "))
if(n<0):
    print(n,"no es un número natural")
else:
    suma=0
    i=1
    k=0
    while(n-(suma+i)>=0):
        suma=suma+i
        k=k+1
        i=i+2
    print("La xx de",n,"es",k)
    