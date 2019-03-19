#Servicios:                 Operadores          Regiones
#Internet Banda Ancha       Claro               Caribe
#Telefonia Movil            Etb                 Eje Cafetero
#                           Movistar            Andina
#                           Tigo Une            Llano Oriente
#1) Calcular las multas de cada operador.
#2) El operador con el mayor valor en multas.
#3) La region con menos valor en multas.
#4) promedio de las multas del eje cafetero.
#5) las dos regiones con menos multas por prestacion del servicio internet de banda ancha.
import random
import numpy as np
def Print(x,y,z):
    if(x==1):
        print("Operador: Claro")
    elif(x == 2):
        print("Operador: ETB")
    elif(x == 3):
        print("Operador: Movistar")
    elif(x == 4):
        print("Operador: Tigo Une")

    if(y == 1):
        print("Servicio: Internet Banda Ancha")
    elif(y == 2):
        print("Servicio: Telefonia Movil")

    if(z == 1):
        print("Region: Caribe")
    elif(z == 2):
        print("Region: Eje Cafetero")
    elif(z == 3):
        print("Region: Andina")
    elif(z == 4):
        print("Region: Llano Oriente")

def val():
    var=random.randrange(100)
    return var

Operadores=[]

for i in range(4):
    ser=[]
    for j in range(2):
        reg=[]
        for f in range(4):
            reg.append(val())
        ser.append(reg)
    Operadores.append(ser)
Operadores=np.array(Operadores)
print()
print("-----------------------------------------------------------")
for i in range(4):
    Print(i + 1, -1, -1)
    print("Total Multas: ",np.sum(Operadores[i]))
print("-----------------------------------------------------------")
Max=0
for i in range(4):
    if(np.sum(Operadores[i])>Max):
        Max=np.sum(Operadores[i])
        pos=i+1
print("El valor mayor de multas lo tiene el ",end="")
Print(pos,-1,-1)
print("-----------------------------------------------------------")
var=np.array([0,0,0,0])
for i in range(4):
    var=var+Operadores[i][0][:] + Operadores[i][1][:]
pos = np.argmin(var)+1
print("El valor Menor de multas lo tiene la ",end="")
Print(-1,-1,pos)
print("-----------------------------------------------------------")
print("El Promedio de la ",end="")
Print(-1,-1,2)
print("Es de: ", end="")
print(var[1]/8)
print("-----------------------------------------------------------")
var=np.array([0,0,0,0])
for i in range(4):
    var=var+Operadores[i][0][:]
print("Las 2 regiones con Menos multas por prestacion del servicio internet de banda ancha son:")
print("1) ",end="")
Print(-1,-1,np.argmin(var)+1)
var[np.argmin(var)]=401
print("2) ",end="")
Print(-1,-1,np.argmin(var)+1)