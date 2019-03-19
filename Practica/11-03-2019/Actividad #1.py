# Numeros Amigos
def Suma_Div(num):
    s=0;
    for i in range(1, (num//2)+1):
        if(num%i==0):
            s=s+i;
    return s;

x=int(input("Digite #1: "))
y=int(input("Digite #2: "))

sumX=Suma_Div(x)
sumY=Suma_Div(y)

if(x==sumY and y==sumX):
    print("Son Amigos")
else:
    print("No Lo Son")
