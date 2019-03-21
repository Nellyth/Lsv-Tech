#El Factor Primo Mayot De un Numero x
num=600851475143
vec=[]
inc=1
while(True):
    inc+=1
    if(num%inc==0):
        vec.append(inc)
        num=num/inc
        inc=1
    if(num/inc==1):
        break
print(vec)
print("El Factor Primo Mayor Es: ",max(vec))