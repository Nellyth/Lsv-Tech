#Promedio de 6 notas ordenados de manera descendente
cant=int(input("Numero de Estudiantes: "));
datos=[]
for i in range(cant):
    var = []
    sum=0
    var.append(input("Digite El Nombre Del Estudiante: "))
    for j in range(6):
        nota=float(input("Digite La Nota: "))
        sum=sum+nota
    var.append(sum/6)
    datos.append(var)

for i in range(cant):
    for j in range(cant):
        if datos[i][1]>datos[j][1]:
            auxNom=datos[i][0]
            auxNt=datos[i][1]
            datos[i][0]=datos[j][0]
            datos[i][1]=datos[j][1]
            datos[j][0]=auxNom
            datos[j][1]=auxNt

print()
print("Mostrando Descendentemente")
for i in range(cant):
    for j in range(2):
        print(datos[i][j]," ",end="")
    print()