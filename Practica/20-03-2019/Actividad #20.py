#Diferencia Entre Una Cuadrado De La Suma - Suma De Cuadrado
sumC=0
cuaS=0
for i in range(1,101):
    sumC+=i**2
    cuaS+=i
cuaS=cuaS**2
print("Suma de cuadrado: ",sumC)
print("Cuadrado de la suma: ",cuaS)
print("La diferencia es de: ",cuaS-sumC)