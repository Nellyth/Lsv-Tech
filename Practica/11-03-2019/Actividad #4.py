#Tweets Estado
msg_Pos=["Bueno","Optimo","Excelente"]
msg_Neg=["Malo","Pesimo","Deficiente"]
cont_pos=0
cont_neg=0
m_tweet=[]

def llenar_matriz_tweets(fecha, cantF):
    m_tweet.append(fecha)
    for i in range(cantF):
        m_tweet.append(input("Ingrese El Tweet: "))


fecha = input("Ingrese la Fecha: ('11/3/2019') ")
cantF=int(input("cantidad de Tweets por fecha "))

llenar_matriz_tweets(fecha,cantF)

for i in range(len(m_tweet)):
    palabra=m_tweet[i].split(" ")
    numP = 0
    numN = 0
    for word in palabra:
        if word in msg_Pos:
            numP=numP+1
        if word in msg_Neg:
            numN=numN+1
    if(numP>numN):
        cont_pos=cont_pos+1
    elif(numP<numN):
        cont_neg=cont_neg+1

print("Contador Positivo de Tweets: ",cont_pos, " Su Porcentaje Es: ",cont_pos/cantF*100,"%")
print("Contador Negativo de Tweets: ",cont_neg, " Su Porcentaje Es: ",cont_neg/cantF*100,"%")
