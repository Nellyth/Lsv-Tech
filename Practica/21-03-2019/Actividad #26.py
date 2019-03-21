#Calcular El salario de los trabajadores dados, dependiendo de la informacion dada por el usuario
#y calcular el pago total de la empresa
listDiccionary=[]

def mostrar():
    Slm = 850000
    AuxT = 72250
    pagoTotalEmpresa=0
    for Diccionary in listDiccionary:
        if (Slm * Diccionary['SM'] <= Slm):
            dic = {'Aux Trans': AuxT}
            Diccionary.update(dic)
        VlHo = round(Slm * Diccionary['SM'] / 240)
        Cesantias = round(Slm * Diccionary['SM'] / 360)
        ICesantias = round((Cesantias * Diccionary['dd'] * 0.12) / 360)
        PServicio = round(Slm * Diccionary['SM'] * 180)
        Vacations = round((Slm * Diccionary['dd']) / 720)
        res = Cesantias + ICesantias + PServicio + Vacations
        Diccionary.update(
            {'Cesantias': Cesantias, 'ICesantias': ICesantias, 'PServicio': PServicio, 'Vacations': Vacations})
        dic = {'Liquidation': res}
        Diccionary.update(dic)
        Hed = round(VlHo * 1.25 * Diccionary['HED'])
        Hn = round(VlHo * 1.35 * Diccionary['HN'])
        Hen = round(VlHo * 1.75 * Diccionary['HEN'])
        Hedf = round(VlHo * 2 * Diccionary['HEDF'])
        Hendf = round(VlHo * 2.5 * Diccionary['HENDF'])
        Diccionary['HED'] = [Diccionary['HED'], Hed]
        Diccionary['HN'] = [Diccionary['HN'], Hn]
        Diccionary['HEN'] = [Diccionary['HEN'], Hen]
        Diccionary['HEDF'] = [Diccionary['HEDF'], Hedf]
        Diccionary['HENDF'] = [Diccionary['HENDF'], Hendf]
        if (Slm * Diccionary['SM'] <= Slm):
            res += AuxT
        res += Hed + Hn + Hen + Hedf + Hendf
        dic = {'Net Paid': res}
        Diccionary.update(dic)
    for Diccionary in listDiccionary:
        pagoTotalEmpresa+=Diccionary['Net Paid']
    listDiccionary.append(pagoTotalEmpresa)

    print()
    print(listDiccionary)
    print()
    for Diccionary in listDiccionary:
        print(Diccionary)
    exit()

def comprobar(name,sm,hed,hn,hen,hedf,hendf,dd):
    if not name:
        print("The Name Can not Be Null")
        return False
    if not sm:
        print("The Field Amount Of SM Can Not Be Null")
        return False
    if not hed:
        print("The Field Amount Of HED Can not Be Null")
        return False
    if not hn:
        print("The Field Number Of HN Can not Be Null")
        return False
    if not hen:
        print("The Field Amount Of HEN Can not Be Null")
        return False
    if not hedf:
        print("The Field Amount Of HEDF Can not Be Null")
        return False
    if not hendf:
        print("The Field Amount Of HENDF Can not Be Null")
        return False
    if not dd:
        print("The Field Amount Of DD Can not Be Null")
        return False

    if not sm.isnumeric():
        print("The SM Field Has To Be Numeric")
        return False
    if not hed.isnumeric():
        print("The HED Field Has To Be Numeric")
        return False
    if not hn.isnumeric():
        print("The HN Field Has To Be Numeric")
        return False
    if not hen.isnumeric():
        print("The HEN Field Has To Be Numeric")
        return False
    if not hedf.isnumeric():
        print("The HEDF Field Has To Be Numeric")
        return False
    if not hendf.isnumeric():
        print("The HENDF Field Has To Be Numeric")
        return False
    if not dd.isnumeric():
        print("The DD Field Has To Be Numeric")
        return False
    return True


while(True):
    print("1: Enter Register: ")
    print("2: Show Record And Finish")
    opcion=input("Select ")
    if(opcion=='1'):
        name = input("Enter The Name? ")
        sm = input("Amount of SM? ")
        hed = input("Amount of Hour Daily Extras? ")
        hn = input("Number of Norturn hours? ")
        hen = input("Amount of Norturn Hour Extras? ")
        hedf = input("Daytime Extra Sunday or Festive? ")
        hendf = input("Nocturna Sunday or Festive Extra Time? ")
        dd = input("Number of days worked? ")
        if(comprobar(name,sm,hed,hn,hen,hedf,hendf,dd)==True):
            listDiccionary.append(dict(zip(['Name','SM','HED','HN','HEN','HEDF','HENDF','dd'],[name,int(sm),int(hed),int(hn),int(hen),int(hedf),int(hendf),int(dd)])))
    elif(opcion == '2'):
        print()
        print("-----------------------------------------------------------------------------------------")
        print("-----------------------------------------------------------------------------------------")
        mostrar()
    else:
        print("Seleccione una opcion Valida")
        print()
