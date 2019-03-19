dato=str(input("digite el texto: "))
texto=dato.lower().replace(" ", "");
def remove_final(texto):
    texto=texto[::-1]
    return texto[ 0:len(texto) - 1]

def remove_inicial(texto):
    return texto[1 : len(texto)]

if(texto[::-1]==texto):
    print("Es palindrome")
ant=0
recurencia=0
if(texto[::-1]!=texto):
    for i in range(len(texto)):
        if(remove_final(texto)==remove_inicial(texto)):
            if(ant<len(texto)):
                ant = len(texto)
                recurencia=len(texto)

    if(recurencia*100/len(dato)>=80):
        print("Tiene Un Porcentaje De: ",round(recurencia*100/len(dato)),"%")
    else:
        print("No Es Palindrome")
