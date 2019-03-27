# crear una agenda con clases, se puede pedir n datos hasta que el usuario no desee ingresar mas,
# kwargs: Direccion, Whatsapp: True | False, Telegram: True | False.
cont = 1;

class Agenda():
    agenda = []
    def guardar_contacto(self, id, name, phone, **kwargs):
        self.agenda.append([id, name, phone, kwargs])

    def editar_conctacto(self,nombre):
        for i in self.agenda:
            if i[1] == nombre:
                num=self.agenda.index(i)
                eliminar = Agenda()
                eliminar.eliminar_contacto(nombre)
                return num

    def eliminar_contacto(self, nombre):
        for i in self.agenda:
            if i[1] == nombre:
                self.agenda.remove(i)

    def listar_contacto(self, *args):
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

class Contactos():
    def contacto(self,name,*args):
        print()
        print("-----------------------------------------")
        for i in args[0]:
            if(name==i[1]):
                print('ID: {}'.format(i[0]))
                print('Nombre: {}'.format(i[1]))
                print('Telefono: {}'.format(i[2]))
                print('Direccion: {Direccion}'.format(**i[3]))
                print('Whatsapp: {Whatsapp}'.format(**i[3]))
                print('Telegram: {Telegram}'.format(**i[3]))
                print("-----------------------------------------")

def PedirDatos(num):
    phone = []
    name = input("Nombre de usuario? ")
    number_phone = int(input("Telefono? "))
    phone.append(number_phone)
    while (True):
        print('Desea Añadir Otro Telefono')
        res = input('si || no? ')
        if (res == 'si'):
            number_phone = int(input("Telefono? "))
            phone.append(number_phone)
        elif (res == 'no'):
            break
        else:
            print('Respuesta Invalidad')
        print()
    Direccion = input("Direccion? ")
    print('no null = True, null = False ')
    whatsapp = bool(input("whatsapp? "))
    telegram = bool(input("Telegram? "))
    return num,name,phone,Direccion,whatsapp,telegram

while (True):
    print("1: Ingresar Registro: ")
    print("2: Editar Contacto: ")
    print("3: Eliminar Contacto: ")
    print("4: Mostrar Registro")
    print("5: Mostrar Un Contacto")
    print("6: Salir")

    opcion = input("Seleccione ")
    if (opcion == '1'):
        num, name, phone, Direccion, whatsapp, telegram = PedirDatos(cont)
        guardar = Agenda()
        guardar.guardar_contacto(cont, name, phone, Direccion=Direccion, Whatsapp=whatsapp, Telegram=telegram)
        cont += 1
    elif (opcion == '2'):
        nombre = input('digite el nombre del contacto a Editar: ')
        print()
        Edit = Agenda()
        num = Edit.editar_conctacto(nombre)
        num,name,phone,Direccion,whatsapp,telegram=PedirDatos(num)
        guardar = Agenda()
        guardar.guardar_contacto(num+1, name, phone, Direccion=Direccion, Whatsapp=whatsapp, Telegram=telegram)
    elif (opcion == '3'):
        nombre = input('digite el nombre del contacto a eliminar: ')
        print()
        delete = Agenda()
        delete.eliminar_contacto(nombre)
    elif (opcion == '4'):
        listar = Agenda()
        listar.listar_contacto(listar.agenda)
    elif (opcion == '5'):
        name=input('Digite El Nombre Del Contacto A Buscar? ')
        data = Agenda()
        con = Contactos()
        con.contacto(name,data.agenda)
    elif (opcion == '6'):
        exit()
    else:
        print("Seleccione una opción Valida")
        print()