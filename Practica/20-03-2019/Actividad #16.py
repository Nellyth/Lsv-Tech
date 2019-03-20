num=1
v=1
sum=0
for i in range(50):
    ant=num
    num=v
    v=ant+num
    print(num,end=" || ")
    if(num%2==0):
        sum=sum+num
    if(4000000<v):
        break
print()
print("El Resultado Es: ",sum)