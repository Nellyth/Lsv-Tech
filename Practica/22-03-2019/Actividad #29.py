cont=2
def div(num):
    vec = []
    inc = 1
    while (True):
        if (num % inc == 0):
            vec.append(inc)
        if (inc >= num/2):
            break
        inc += 1
    vec.append(num)
    return vec

sm=0
while (True):
    sm+=cont
    if(len(div(sm))>=500):
        print(div(sm))
        break
    cont+=1
    print(sm," cantidad: ",len(div(sm)))
