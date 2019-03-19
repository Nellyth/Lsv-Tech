import math
x=int(input("Ingrese el tamaño del disco duro en gigabyte: "))
x=x*1024
x=x/700
x=math.ceil(x)
print("La Cantidad De CDs Que Necesita Es: ",x);
