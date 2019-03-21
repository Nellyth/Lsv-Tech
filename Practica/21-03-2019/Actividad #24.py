#crear un diccionario donde la clave sea el nombre y el valor sea el telefono, se puede pedir n datos hasta que el
#usuario no desee ingresar mas, NO SE PUEDEN REPETIR DATOS.

diccionary={}

def datos(key, value):
    if( not key or not value):
        print("El Usuario O Telefono No Pueden Estar Vacios")
        print()
        return
    if(value.isnumeric()==False):
        print("El Telefono Tiene Que Ser Numerico")
        print()
        return
    if(key in diccionary.keys()):
        print("El Usuario Ya Existe")
        print()
        return
    if (value in diccionary.values()):
        print("El Telefono Ya Existe")
        print()
        return
    diccionary.setdefault(key, int(value))

while(True):
    print("1: Ingresar Registro: ")
    print("2: Mostrar Registro Y Finalizar")
    opcion=input("Seleccione ")
    if(opcion=='1'):
        key = input("Nombre de usuario? ")
        value = input("Telefono? ")
        datos(key, value)
    elif(opcion == '2'):
        print()
        print("-----------------------------------------")
        for i in diccionary:
            print(diccionary)
            print("Cantidad de Usuarios: ",len(diccionary.keys()))
            exit()
    else:
        print("Seleccione una opcion Valida")
        print()


