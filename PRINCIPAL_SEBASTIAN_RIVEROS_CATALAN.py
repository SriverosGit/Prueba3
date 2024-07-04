#programa

import FUNCIONES_SEBASTIAN_RIVEROS_CATALAN as fn

lista_nombres = []
lista_direccion = []
lista_dias = []
lista_insumos = []
lista_bonificacion = []
lista_total_pago = []


while True:
    print("1.-Registrar cobro.")
    print("2.-Listar cobros registrados.")
    print("3.-Definir sector de despacho.")
    print("4.-Salir.")
    
    opcion = int(input("Ingrese una opcion: "))
    if opcion ==1:
        fn.registro(lista_nombres, lista_direccion, lista_dias, lista_insumos, lista_bonificacion, lista_total_pago)
    elif opcion ==2:
        fn.listar_pacientes(lista_nombres, lista_direccion, lista_dias, lista_insumos, lista_bonificacion, lista_total_pago)
    elif opcion ==3:
        pass
    elif opcion ==4:
        break
    



