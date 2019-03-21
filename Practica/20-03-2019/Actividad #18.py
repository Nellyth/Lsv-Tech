#Numero Palindromico de 3 Cifras
vec=[0,0,0]
for i in range(100,1000):
    for j in range(100, 1000):
        res=i*j
        if(str(res)[::-1]==str(res)):
            if(res>vec[2]):
                vec[0]=i
                vec[1]=j
                vec[2]=res

print("El Maximo Es Numero Palindrómico de 3 cifras Es: ",vec[2],"=",vec[0],"*",vec[1])
