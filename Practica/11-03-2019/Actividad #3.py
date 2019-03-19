#Numeros Primos

def numeroPrimo(num):
    sum=0;
    for i in range(1,(num//2+1)):
        if(num%i==0):
            sum=sum+1;
    if(sum==1):
        return num;
    else:
        return 0;

z=int(input("Digite un numero minimo del rango: "));
x=int(input("Digite un numero maximo del rango: "));
for i in range(z,x+1):
    v=numeroPrimo(i);
    if(v!=0):
        print(v);