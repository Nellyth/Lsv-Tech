class Class_Agencias:

    def __init__(self, Codigo, Nombre, Direccion, Conductores):
        self.Codigo = Codigo
        self.Nombre = Nombre
        self.Direccion = Direccion
        self.Conductores = Conductores


class Class_Turistas:

    def __init__(self, Codigo, Identificacion, Nombre, Apellido, Nacionalidad, Sexo, Edad):
        self.Codigo = Codigo
        self.Identificacion = Identificacion
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Nacionalidad = Nacionalidad
        self.Sexo = Sexo
        self.Edad = Edad


class Class_Conductores:

    def __init__(self, Codigo, Identificacion, Nombre, Apellido, Sexo, Edad, Nacionalidad, Codigo_Agencia):
        self.Codigo = Codigo
        self.Identificacion = Identificacion
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Sexo = Sexo
        self.Edad = Edad
        self.Nacionalidad = Nacionalidad
        self.Codigo_Agencia = Codigo_Agencia


class Class_Tours:

    def __init__(self, Codigo, Destino, Fecha, Costo, Duracion, Codigo_Conductores, Turista):
        self.Codigo = Codigo
        self.Destino = Destino
        self.Fecha = Fecha
        self.Costo = Costo
        self.Duracion = Duracion
        self.Codigo_Conductores = Codigo_Conductores
        self.Turista = Turista


class Class_Consultas:
    def Tour_Mayor_Duracion_Mes(self, args):
        temp = {}
        for i in args:
            data = i.Fecha.split('/')
            may = 0
            for j in args:
                data2 = j.Fecha.split('/')
                if (int(data[1]) == int(data2[1]) and int(data[2]) == int(data2[2])):
                    if (i.Duracion <= j.Duracion):
                        may = j.Duracion
            if not (i.Fecha in temp.keys()):
                temp.setdefault(i.Fecha, may)
        print('Mayor Duracion De Tours Por Mes: ', temp)
        print()

    def Agrupado_tour_mes(self, args):
        temp = {}
        for i in args:
            data = i.Fecha.split('/')
            vec = []
            for j in args:
                data2 = j.Fecha.split('/')
                if (int(data[1]) == int(data2[1]) and int(data[2]) == int(data2[2])):
                    vec.append(j.__dict__)
            if not (i.Fecha in temp.keys()):
                temp.setdefault(i.Fecha, vec)
        for fecha in temp:
            print(
                '----------------------------------------------Agrupado Por Mes: {}----------------------------------------------'.format(
                    fecha))
            for data in temp[fecha]:
                print(data)
            print()
        print()

    def Total_Conductores(self, args):
        print('Total Conductores: {}'.format(len(args)))

    def Total_Turistas(self, args):
        print('Total Turistas: {}'.format(len(args)))
        print()

    def Agrupar_Turistas_Sexo_Nacionalidad(self, args):
        temp = {}
        for i in args:
            vec = []
            if not (i.Nacionalidad in temp.keys()):
                for j in args:
                    if (i.Sexo == j.Sexo and i.Nacionalidad == j.Nacionalidad):
                        vec.append(j.__dict__)
                temp.setdefault(i.Nacionalidad, [{i.Sexo: vec}])
            elif i.Nacionalidad in temp.keys():
                if not (i.Sexo in temp[i.Nacionalidad][0]):
                    for j in args:
                        if (i.Sexo == j.Sexo and i.Nacionalidad == j.Nacionalidad):
                            vec.append(j.__dict__)
                    temp[i.Nacionalidad][0].update({i.Sexo: vec})
        for Nacionalidad in temp:
            print(
                '--------------------------------------------Agrupado Por Nacionalidad: {}--------------------------------------------'.format(
                    Nacionalidad))
            for Turista_Nacionalidad in temp[Nacionalidad]:
                for Sexo in Turista_Nacionalidad:
                    print('{}:'.format(Sexo))
                    for Turista_Sexo in Turista_Nacionalidad[Sexo]:
                        print('      {}'.format(Turista_Sexo))
            print()

    def Agrupar_Tours_Por_Agencia(self, Tours,Conductores,Agencia):
        print('----------------------------------------Agrupacion De Tours Por Agencia----------------------------------------')
        for i in Agencia:
            for j in Conductores:
                if i.Codigo==j.Codigo_Agencia:
                    for a in Tours:
                        if j.Codigo==a.Codigo_Conductores:
                            print('Nombre de la agencia: {}, Destino del Tours: {}'.format(i.Nombre,a.Destino))


print()

Data_Agencia = []
Data_Agencia.append(Class_Agencias('1', 'ThunderBlack', 'Cartagena', ['1']))
Data_Agencia.append(Class_Agencias('2', 'Pitacus', 'Santa Marta', ['2']))
Agencia = Data_Agencia

Data_Turistas = []
Data_Turistas.append(Class_Turistas('1', '45654', 'Andres', 'Tijeras', 'Francia', 'Male', '20'))
Data_Turistas.append(Class_Turistas('2', '7894', 'Luis', 'Kanji', 'Ecuador', 'Male', '25'))
Data_Turistas.append(Class_Turistas('3', '554488', 'Lissett', 'Gonzales', 'Francia', 'Female', '20'))
Turistas = Data_Turistas

Data_Conductores = []
Data_Conductores.append(Class_Conductores('1', '1044934747', 'Nellyth', 'Arroyo', 'Male', '21', 'Colombia', '1'))
Data_Conductores.append(Class_Conductores('2', '30762111', 'Ana', 'Martinez', 'Female', '18', 'Colombia', '2'))
Conductores = Data_Conductores

Data_Tours = []
Data_Tours.append(Class_Tours('1', 'Colombia', '27/03/2019', 1624000, 20, '1', ['1', '2']))
Data_Tours.append(Class_Tours('2', 'Canada', '27/04/2019', 2000000, 30, '2', ['1', '2', '3']))
Data_Tours.append(Class_Tours('3', 'Paris', '27/03/2019', 3000000, 25, '1', ['1', '2']))
Tours = Data_Tours

data = Class_Consultas()
data.Tour_Mayor_Duracion_Mes(Tours)
data.Agrupado_tour_mes(Tours)
data.Total_Conductores(Conductores)
data.Total_Turistas(Turistas)
data.Agrupar_Turistas_Sexo_Nacionalidad(Turistas)
data.Agrupar_Tours_Por_Agencia(Tours,Conductores,Agencia)
