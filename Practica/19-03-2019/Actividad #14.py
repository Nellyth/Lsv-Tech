#Pediatrico: nombre del equipo, partidos *jugados *ganados *empatados *perdido, goles *a favor *en contra, tabla de posiciones ordenar decendiente
#puntos: *partidos ganados:3, *partidos empatados:1
equi=[]
def ordenar(cantE):
    for i in range(cantE):
        for j in range(cantE):
            if(((equi[i][6]) > (equi[j][6])) or ((equi[i][6]) == (equi[j][6]))
                    and (equi[i][7]>equi[j][7])):
                aux=equi[i]
                equi[i]=equi[j]
                equi[j]=aux

cantE = int(input("Cantidad de equipos: "))
partJug = int(input("Cantidad de partidos jugados por equipo: "))
for i in range(cantE):
    var = []
    var.append(input("Digite el Nombre del equipo #{}: ".format(str(i + 1))))
    while (True):
        partGan = int(input("Cantidad de partidos ganados por el equipo {}: ".format(var[0])))
        if (partGan <= partJug):
            break
    var.append(partGan)
    if (partGan != partJug):
        while (True):
            partEmp = int(input("Cantidad de partidos Empatados por el equipo {}: ".format(var[0])))
            if (partGan + partEmp <= partJug):
                break;
    else:
        partEmp = 0;
    var.append(partEmp)
    partPer = partJug - (partGan + partEmp)
    var.append(partPer)
    GolAf=int(input("Goles a Favor del equipo {}: ".format(var[0])))
    GolEnc=int(input("Goles en Contra del equipo {}: ".format(var[0])))
    var.append(GolAf)
    var.append(GolEnc)
    var.append(partGan*3+partEmp)
    var.append(GolAf-GolEnc)
    equi.append(var)

ordenar(cantE)
print("  Nombre del Equipo |  Partidos Ganados  | Partidos Empatados | Partidos  Perdidos |   Goles A Favor    |   Goles En Contra   |      Puntos       |  Puntuacion Goles  ")
for i in range(cantE):
    for j in range(len(equi[i])):
        mitad=(20-len(str(equi[i][j])))//2
        for k in range(mitad):
            print(" ",end="")
        print(equi[i][j],end="")
        for k in range(mitad):
            print(" ",end="")
        if((20-len(str(equi[i][j])))%2!=0):
            print(" ",end="")
        print(" ", end="")
    print()