#consumo de la gasolina(litros y euros) por cada 100km
#consumo de la gasolina(litros y euros) por cada km
#velocidad media (km/s y m/s)
Kr = int(input("Kilometros recorridos: "))
Pgl = int(input("Precio de la Gasolina * Litro: "))
Cdgv = int(input("Cantidad de dinero gastado en el viaje en pesos: "))
while(True):
    thm = input("Tiempo tardados en Horas y minutos, ej: 3:40 ")
    thm = thm.split(":")
    if((thm[0].isnumeric()==True) and (thm[1].isnumeric()==True)):
        if(int(thm[0])>=0 and (int(thm[1])>=0 and int(thm[1])<=60)):
            break


seg=int(thm[0])*3600+int(thm[1])*60
kms=Kr/(seg*3600)
ms=(Kr*1000)/seg
pck100=(((Cdgv/Pgl)/Kr)*100)
pck=((Cdgv/Pgl)/Kr)

print()
print("Consumo de litros por Km: ", pck)
print("Precio en euro por km: ",(pck*Pgl)*0.00028)

print()
print("Consumo de litros por cada 100 Km: ", pck100)
print("Precio en euro por cada 100 km: ",(pck100*Pgl)*0.00028)

print()
print("Velocidad media por km/h: ",kms)
print("Velocidad media por m/s: ",ms)
