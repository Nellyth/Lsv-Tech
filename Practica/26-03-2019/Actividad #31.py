#crear una agenda, se puede pedir n datos hasta que el usuario no desee ingresar mas,
# kwargs: Direccion, Whatsapp: True | False, Telegram: True | False.
cont=1;
agenda=[]

def listar_contactos(*args):
    print()
    print("-----------------------------------------")
    for i in args[0]:
        print('ID: {}'.format(i[0]))
        print('Nombre: {}'.format(i[1]))
        print('Telefono: {}'.format(i[2]))
        print('Direccion: {Direccion}'.format(**i[3]))
        print('Whatsapp: {Whatsapp}'.format(**i[3]))
        print('Telegram: {Telegram}'.format(**i[3]))
        print("-----------------------------------------")

    print("Cantidad de Usuarios: ", len(agenda))
    exit()

def save_contact(id,name,phone,**kwargs):
    agenda.append([id,name,phone,kwargs])

def Phone(number_phone):
    phone.append(number_phone)

while(True):
    print("1: Ingresar Registro: ")
    print("2: Mostrar Registro Y Finalizar")
    opcion=input("Seleccione ")
    if(opcion=='1'):
        phone=[]
        name = input("Nombre de usuario? ")
        number_phone = int(input("Telefono? "))
        Phone(number_phone)
        while(True):
            res = ''
            print('Desea Añadir Otro Telefono')
            res=input('si || no? ')
            if(res == 'si'):
                number_phone = int(input("Telefono? "))
                Phone(number_phone)
            elif(res=='no'):
                break
            else:
                print('Respuesta Invalidad')
        Direccion = input("Direccion? ")
        print('no null = True, null = False ')
        whatsapp = bool(input("whatsapp? "))
        telegram = bool(input("Telegram? "))
        save_contact(cont,name,phone,Direccion=Direccion,Whatsapp=whatsapp,Telegram=telegram)
        cont+=1
    elif(opcion == '2'):
        listar_contactos(agenda)
    else:
        print("Seleccione una opción Valida")
        print()