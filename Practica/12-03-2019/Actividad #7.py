#Dada una Matriz impar generar el cuadrado magico
tam=int(input("Tamaño de la matriz: "))
cuadMagic=[]
for i in range(tam):
    vet=[];
    for j in range(tam):
        vet.append(0)
    cuadMagic.append(vet)

i=0
j=len(cuadMagic[0])//2
max=len(cuadMagic[0])-1
for z in range(1, tam*tam+1):
    cuadMagic[i][j]=z
    i=i-1
    j=j+1
    if(i==-1):
        i=max
    if(j==max+1):
        j=0
    if (cuadMagic[i][j]!= 0):
        if (i == -1):
            i = max
        if (j == max + 1):
            j = 0
        if(i==max and j==0):
            i=0
            j = max
            i=i+1
            cuadMagic[i][j] = z
        else:
            i = i + 2
            j = j - 1
            if (i ==-1):
                i = max
            if (j == max+1):
                j = 0
for i in range(tam):
    print("")
    for j in range(tam):
        print("|",end="")
        mitad = (4 - len(str(cuadMagic[i][j]))) // 2
        for k in range(mitad):
            print(" ",end="")
        print(cuadMagic[i][j],end=" ")
        for k in range(mitad):
            print(" ",end="")
        if((4-len(str(cuadMagic[i][j])))%2!=0):
            print(" ",end="")
    print("|", end="")