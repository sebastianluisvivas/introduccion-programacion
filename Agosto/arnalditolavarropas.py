# Arnaldito lleva cada semana su ropa sucia a un lavadero, y quiere saber si le conviene o no comprar un lavarropas para su casa. La casa de electrodomésticos le ofrece las siguientes alternativas de pago:
# •	en 6 cuotas sin interés, al mismo precio de contado
# •	en 12 cuotas, sumando un 30% al precio de contado
# •	en 18 cuotas, sumando un 50% al precio de contado.
# Arnaldito prefiere pagarlo en el menor tiempo posible, siempre que el monto de la cuota no supere al doble de lo que gasta actualmente por mes en el lavadero.
# Hacer un programa que ayude a decidir a Arnaldito si puede comprar el lavarropas, o si debe seguir llevando la ropa al lavadero. Se debe mostrar cuál es la decisión 
# y, en el caso de que lo compre, cuál es el monto de la cuota y en cuántos meses lo va a pagar. Se cuenta con los siguientes datos de entrada:

cantLavados=int(input("Ingrese la cantidad de lavados que hace en un mes "))
costoLavadero=float(input("Ingrese el costo de cada lavado en el lavadero automático "))
precioContado=float(input("Ingrese el precio de contado del lavarropas "))
if (precioContado<((cantLavados*costoLavadero)*2)):
    print("Arnaldito comprará el lavarropas al contado por un total de $",precioContado)
else:
    if((((precioContado*0.30)+precioContado)/12)<cantLavados*costoLavadero):
        vc=(((precioContado*0.30)+precioContado)/12)
        pf=vc+precioContado
        print("Le conviene comprar el lavarropas en 12 cuotas de $",vc,"con precio final de $",(round,pf,3))
    else:
        if((((precioContado*0.50)+precioContado)/18)<cantLavados*costoLavadero):
            vc=(((precioContado*0.50)+precioContado)/18)
            pf=vc+precioContado
            print("Le conviene comprar el lavarropas en 18 cuotas de $",vc,"con precio final de $",(round,pf,3))
        else:
            print("Le conviene no comprar el lavarropas y continuar lavando en el lavadero")


            ## Falta revisar el ejercicio en general, y principalmente redondear bien utilizar bien {precioContado+vc.3f}
            # Quiero que quede tres numeros despues de la coma 