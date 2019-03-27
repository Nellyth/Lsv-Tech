#Polimorfismo
#---------------------------------------------------------------------------------------
class A:
    id = 1


class B:
    num = 2


class C:
    def saludar(self,nombre):
        return "Hola {}".format(nombre)

    id = 3


class M(A, B, C):
    pass


print(M.mro())
print(M.id)
print(M.num)
data=M()
print(data.saludar('Nellyth'))

#---------------------------------------------------------------------------------------
class A:
    def sayhi(self):
        print("A")


class B:
    def sayhi(self):
        print("B")


class M(A, B):
    pass


data=M()
data.sayhi()

#---------------------------------------------------------------------------------------
class Propiedad():
    Nombre=''
    def __init__(self):
        self.Nombre='Nellyth'

data = Propiedad()
print('El Nombre Guardado Es: {}'.format(data.Nombre))


#---------------------------------------------------------------------------------------
class Perro():
    color = 'Marron'
    def __init__(self,raza):
        self.raza = raza

print()
pincher = Perro('Pinchers')
print(pincher.raza)
print(pincher.color)

Perro.color='Negro'

pitbull = Perro('Pitbull Americado')
print(pitbull.raza)
print(pitbull.color)