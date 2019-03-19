chof=[]
total=0;
num=5
def choferes(cant):
    for i in range(cant):
        sum=0
        datos=[]
        datos.append(input("Digite el nombre del chofer: "))
        datos.append(input("Cual es el sueldo por Hora del trabjador {}: ".format(datos[0])))
        for j in range(6):
            hora=int(input("Digite Las horas trabajadas por el trabajador {} el dia #{}: ".format(datos[0],str(j+1))))
            sum=sum+hora
            datos.append(hora)
        datos.append(sum)
        datos.append(sum*int(datos[1]))
        chof.append(datos)


Namecom=input("Nombre de la compañia: ")
choferes(num)

print("      Nombre      | Sueldo Por Horas |      Dia #1      |      Dia #2      |      Dia #3      |      Dia #4      |      Dia #5      |      Dia #6      "
      "|    Total Horas   |  Sueldo Semanal  |")
for i in range(num):
    for j in range(len(chof[i])):
        mitad=(18-len(str(chof[i][j])))//2
        for k in range(mitad):
            print(" ",end="")
        print(chof[i][j],end="")
        for k in range(mitad):
            print(" ",end="")
        if((18-len(str(chof[i][j])))%2!=0):
            print(" ",end="")
        print(" ", end="")
    print()

for i in range(num):
    total = total + chof[i][len(chof[i])-1]
    for j in range(num):
        if (chof[i][len(chof[i]) - 4] < chof[j][len(chof[i]) - 4]):
            aux = chof[i]
            chof[i] = chof[j]
            chof[j] = aux
print("La empresa {} Pagara un total de: {}".format(Namecom,total))
print("El Trabajador Con Menos Horas El Viernes Es: ",chof[0][0])
