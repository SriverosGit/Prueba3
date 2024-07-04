#funciones

import csv

lista_sector = []
lista_nombres = []
lista_direccion = []
lista_dias = []
lista_insumos = []
lista_bonificacion = []
lista_total_pago = []
valor_dia = 90000
valor_dias = 0


def registro(lista_nombres, lista_direccion, lista_dias, lista_insumos, lista_bonificacion, lista_total_pago):
    print("-----------Registro-----------")
    nombre = input("Ingrese nombre: ").upper()
    lista_nombres.append(nombre)

    direccion = input("Ingrese direccion: ").upper()
    lista_direccion.append(direccion)
    
    sector = input("Ingrese el sector de la ciudad (Centro,Norte o Sur): ").upper()
    while sector not in ["CENTRO", "NORTE", "SUR"]:
        print("Sector ingresado no es valido, debe ser uno de los indicados anteriormente")
        pass
        sector = input("Ingrese el sector de la ciudad (Centro,Norte o Sur): ").upper()
    lista_sector.append(sector)

    dias=0
    while not (1 <= dias <= 15000):
        try: 
            dias = int(input("Ingrese la cantidad de días: "))
        except ValueError:
                print("Ingrese un numero valido")
        lista_dias.append(dias)
        total_pago = (dias*valor_dia)
        lista_total_pago.append(total_pago)

                
    insumos= 0
    while not (1 <= insumos <= 50000000):
        try:
            insumos = int(input("Ingrese el monto de insumos: "))
            lista_insumos.append(insumos)
        except ValueError:
            print("Ingrese un monto valido")

    bonificacion = int(input("Ingrese monto de la bonificacion: "))
    lista_bonificacion.append(bonificacion)

    





def listar_pacientes(lista_nombres, lista_direccion, lista_dias, lista_insumos, lista_bonificacion, lista_total_pago):
    print("------------Registro-------------")
    print("Nombre\tDireccion\tDias Hospitalizacion\tInsumos\tBonificacion\tTotal")
    for i in range(len(lista_nombres)):
        print(f"{lista_nombres[i]}\t{lista_direccion[i]}\t{lista_dias[i]}\t{lista_insumos[i]}\t{lista_bonificacion[i]}\t{lista_total_pago[i]}")











