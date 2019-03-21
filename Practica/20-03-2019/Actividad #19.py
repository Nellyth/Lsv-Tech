#Buscar Un Numero Que Al Dividirlo Del 1 Hasta El 20 No De Resultado
v=0
sum=0
while(True):
    v+=20
    if(v%2==0 and v%3==0 and v%4==0 and v%5==0 and v%6==0 and v%7==0 and v%8==0 and v%9==0 and
        v%10==0 and v%11==0 and v%12==0 and v%13==0 and v%14==0 and v%15==0 and v%16==0 and
        v%17==0 and v%18==0 and v%19==0 and v%20==0):

        print("El Resultado Es: ", v)
        break
    sum=0