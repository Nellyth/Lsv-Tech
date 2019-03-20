vec=[]
for i in range(1,32):
    vec.append(i**2)
print(vec)
print("")

for i in vec:
    for j in vec:
        if 1000-i+j in vec:
            #print((i+j)+(1000-i+j))
            if(vec.index(i)+vec.index(j)<32):
                print(vec.index(i))
                print(vec.index(j))
                print(vec.index(i)+vec.index(j))
                print()
