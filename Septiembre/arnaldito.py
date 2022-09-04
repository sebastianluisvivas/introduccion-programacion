pronostico=float(input("Ingrese la probabilidad de que llueva "))
chicos=int(input("Indique cuantos chicos confirmaron que vienen "))
costoHamburgesas=5  	#cada chico come 3
costoPancho=2 		#cada chico come 4
peloteroGrande=500
peloteroChico=300
dinero=1000

# Comida
cph=(chicos*5)*3
cpp=(chicos*2)*4
print(cph)

# Pelotero dentro
if (pronostico>65):
    print("Se realizará dentro de la casa y se utilizará un pelotero chico")
    gasto=peloteroChico+cph

    print("Le sobra de dinero:", dinero-gasto)
    if (dinero>=gasto):
        print("Adentro de la casa y pelotero chico con hamburguesas")
        print("Le sobra de dinero:", dinero-gasto)
    else:
        gasto=peloteroChico+cpp
        if (dinero>gasto):
            print("Adentro de la casa y pelotero chico con panchos")
            print("Le sobra de dinero:", dinero-gasto)
        else:
            print("El dinero no alcanza")

# Pelotero afuera
if(pronostico<65):
    if(cph<=500):
        print("Se hará afuera con hamburguesas y pelotero grande")
        resto=(dinero-(cph+500))
        print("Le sobra de dinero:", resto)
    else:
        if(cpp<=700):
            print("Se hará afuera con pelotero grande y panchos")
            resto=(dinero-(cpp+300))
            print("Le sobra de dinero:", resto)
            if(cpp<=500):
                print("Se hará afuera con pelotero chico y hamburguesas")
                resto=(dinero-(cph+300))
                print("Le sobra de dinero:", resto)
            else:
                if(cph<=700):
                    print("Se hará afuera con pelotero chico y panchos")
                    resto=(dinero-(cpp+300))
                    print("Le sobra de dinero:", resto)
                else:
                    print("No le alcanza")
            






    

