#Paseo del caballo

fl=int(input("Digite La posición de la fila: "))
col=int(input("Digite La posición de la columna: "))
matriz=[]
for i in range(8):
    matriz.append([0,0,0,0,0,0,0,0])
matriz[fl][col]=1

def comprobar(ds):
    comp = []
    for det in ds:
        cont = 0
        if (det[0] - 1 >= 0 and det[1] - 2 >= 0):
            if (matriz[det[0] - 1][det[1] - 2] == 0):
                cont = cont + 1

        if (det[0] + 1 <= 7 and det[1] - 2 >= 0):
            if (matriz[det[0] + 1][det[1] - 2] == 0):
                cont = cont + 1

        if (det[0] - 1 >= 0 and det[1] + 2 <= 7):
            if (matriz[det[0] - 1][det[1] + 2] == 0):
                cont = cont + 1

        if (det[0] + 1 <= 7 and det[1] + 2 <= 7):
            if (matriz[det[0] + 1][det[1] + 2] == 0):
                cont = cont + 1

        if (det[0] - 2 >= 0 and det[1] - 1 >= 0):
            if (matriz[det[0] - 2][det[1] - 1] == 0):
                cont = cont + 1

        if (det[0] + 2 <= 7 and det[1] - 1 >= 0):
            if (matriz[det[0] + 2][det[1] - 1] == 0):
                cont = cont + 1

        if (det[0] - 2 >= 0 and det[1] + 1 <= 7):
            if (matriz[det[0] - 2][det[1] + 1] == 0):
                cont = cont + 1

        if (det[0] + 2 <= 7 and det[1] + 1 <= 7):
            if (matriz[det[0] + 2][det[1] + 1] == 0):
                cont = cont + 1
        comp.append(cont)
    return comp

def mov(fila,column):
    det=[]
    if(fila-1>=0 and column-2>=0):
        if (matriz[fila - 1][column - 2] == 0):
            det.append([fila-1,column-2])

    if(fila+1<=7 and column-2>=0):
        if (matriz[fila + 1][column - 2] == 0):
            det.append([fila+1, column-2])

    if(fila-1>=0 and column+2<=7):
        if (matriz[fila - 1][column + 2] == 0):
            det.append([fila-1,column+2])

    if(fila+1<=7 and column+2<=7):
        if (matriz[fila + 1][column + 2] == 0):
            det.append([fila+1,column+2])

    if(fila-2>=0 and column-1>=0):
        if (matriz[fila - 2][column - 1] == 0):
            det.append([fila-2,column-1])

    if(fila+2<=7 and column-1>=0):
        if (matriz[fila + 2][column - 1] == 0):
            det.append([fila+2,column-1])

    if(fila-2>=0 and column+1<=7):
        if (matriz[fila - 2][column +1] == 0):
            det.append([fila-2,column+1])

    if(fila+2<=7 and column+1<=7):
        if (matriz[fila +2][column +1] == 0):
            det.append([fila+2,column+1])
    return det

#movimientos
#i-1,j-2
#i+1,j-2
#i-1,i+2
#i+1,j+2
#i-2,j-1
#i+2,j-1
#i-2,j+1
#i+2,j+1
z=1
while(True):
    min=9
    pos=0
    z+=1
    for i in range(len(comprobar(mov(fl,col)))):
        var=comprobar(mov(fl,col))
        if(var[i]<min):
           min=var[i]
           pos = i;
    var=mov(fl, col)
    matriz[var[pos][0]][var[pos][1]]=z
    fl=var[pos][0]
    col=var[pos][1]
    if(z==64):
        break


for i in range(8):
    print("")
    for j in range(8):
        print("|",end="")
        mitad = (4 - len(str(matriz[i][j]))) // 2
        for k in range(mitad):
            print(" ",end="")
        print(matriz[i][j],end=" ")
        for k in range(mitad):
            print(" ",end="")
        if((4-len(str(matriz[i][j])))%2!=0):
            print(" ",end="")
    print("|", end="")

