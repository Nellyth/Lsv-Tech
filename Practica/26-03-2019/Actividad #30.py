#Entrenando funciones con el * y el doble *, ademas de la agregacion del .format

list = [2,3,4,5]
Usuarios={'Nellyth':123456,'Ana':654321}

#Funcion De Orden Superior
def authenticate(usuario, password):
    def validate(usuario, contraseña):
        if not(usuario in Usuarios.keys()):
            return "El Usuario No Existe"
        else:
            if not(Usuarios[usuario]==password):
                return 'Contraseña Errada'
            else:
                return login(usuario)
    def login(usuario):
        return 'Se A Logueado Exitosamente con el Usuario {}'.format(usuario)
    return validate(usuario,password)
print()
print('------------------------------------------')
print(authenticate('Nellyth',123456))
print(authenticate('Nellyth',234))
print(authenticate('Nellth',123456))
print('------------------------------------------')
print()
#------------------------
def text_argument(*args):
    print(args)

def text_key_argument(**krargs):
    print(krargs)

def sumador(*args):
    return sum(args)

def saludo(**krargs):
    pais=krargs.get('Nacionalidad','Colombiano')
    if(pais=='Colombiano'):
        return 'Hola, Mi Nombre es {Name} Y Mi Edad Es De {Edad} años Y Soy Colombiano'.format(**krargs)
    else:
        return 'Hola, Mi Nombre es {Name} Y Mi Edad Es De {Edad} años'.format(**krargs)

text_argument(list)
text_key_argument(name='Nellyth',Edad=21,Sexo='Male')
print(sumador(1,2,3,4,5,6,7))
print(saludo(Name='Nellyth',Edad=21,pais='Colombiano'))