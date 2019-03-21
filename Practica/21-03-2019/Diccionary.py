#Practicando Con Diccionario
diccionary = {"Nellyth":["Arroyo Marrugo",21],"Ana":["Steel",18],"Juan":["El Pendejo",50]}
#print("", diccionary["Nellyth"])
diccionary1={"Nellyth":{"Apellido":"Arroyo Marrugo","Edad":21,"Direccion":"Arjona Bolivar","Email":"nellith25@gmail.com","Telefono":"3005184942"}}
#print("", diccionary1["Nellyth"])
print()
for i in diccionary1:
    print("Name: ",i)
    for j in diccionary1[i]:
        print(j,": ",diccionary1[i][j])

#Method dict in tuple
print()
tupla=dict(Name = "Nellyth", lastName = "Arroyo")
print(tupla)

#Method Zip
print()
dato=dict(zip("ABCDEF", [1,2,3,4,5,6]))
print(dato)

#show the items in the dictionary
print()
print(diccionary.items())

#show the keys in the dictionary
print()
print(diccionary.keys())

#shows the dictionary values
print()
print(diccionary.values())

#copy the dictionary
print()
print(diccionary.copy())

#Method Get
print()
print(diccionary.get("Nellyth"))

#delete a data in a position
print()
#print(diccionary.pop())

#delete the data in the dictionary
print()
print(diccionary.clear())

#Method FromKeys
print()
print(dict.fromkeys(['A','B','C'],"Nellyth"))

#Method Setdefault
print()
diccionary.setdefault("Phone","Nellyth")
print(diccionary)

print()
diccionary.update(diccionary1)
print(diccionary)