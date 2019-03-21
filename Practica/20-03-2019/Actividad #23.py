for i in range(1,1001):
    for j in range(i+1,1001):
        for z in range(j+1, 1001):
            if i**2+j**2==z**2 and i+j+z==1000:
                print("A: ",i,"B: ",j,"C: ",z)
                print(i,"+",j,"+",z,"=",i+j+z)
                print(i**2, "+", j**2, "=", z**2)
                exit()
