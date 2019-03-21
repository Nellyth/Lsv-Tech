primo=[2,3,5,7]
def comprobar(num):
    for j in primo:
        if(num%j!=0):
            if(num/j<j):
                primo.append(num)
                return True
        else:
            return False
    return False
sum=0
for i in range(3,2000000):
    if (comprobar(i)==True):
        sum+=i
print(sum+2)
