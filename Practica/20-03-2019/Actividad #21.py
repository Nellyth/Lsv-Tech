def primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

v=2
cont=0
while(True):
    if(primo(v)==True):
        cont+=1
    if(cont==10001):
        print("El número primo 10001st Es: ",v)
        break
    v+=1
