from citas import *
import random as rn
ciclo = True
import numpy as np




def Agragarcita():
    p = citas
    c = False
    while c == False:
        c = p.setregistrar(input("ingrese registro.Ej.A-000:"))
    while c == False:
        c = p.NombreCliente(input("ingrese NombreCliente:"))
    while c == False:
        c = p.descripcionAtencion(input("Ingrese Atencion:"))

def Buscarcita(lista_citas):
    registrar = input("ingrese registro ej.A-000")
    for citas in lista_citas:
        if registrar == citas.registrar:
            flag = True
            print("Datos de la cita:")
            print(f"registro{citas.registrar}")
            print(f"Nombre{citas.NombreCliente}")
            print(f"descripcion{citas.descripcionAtencion}")
            if citas.descripcionAtencion >= 1:
                print("Descripcion de Atencion correcta")
            else:
                print("Descripcion incorrecta")
            break
    if flag == False:
        print("no existe el registro:")


class NombreCliente:
    pass


def Imprimir(lista_citas, descripcionAtencion=None):
    registrar = input("ingrese registro ej.A-000")
    flag = False
    for citas in lista_citas:
        if registrar == citas.registrar:
        match op:
            case 1:
                print("registro")
        print(f"registro:{registrar}")
        print(f"nombre:{NombreCliente}")
        print(f"descripcion:{descripcionAtencion}")
        flag=True

def Salir():
    return False

 while ciclo:
    print("Menu Mechas locas")
    print("1) Grabar cita")
    print("2) Buscar cita")
    print("3) Imprimir atencion")
    print("4) Salir")
    try:
        op=int(input("seleccione (1-4:)"))
        match op:
            case 1:
                print("Grabar cita")
                Agragarcita(Agragarcita)
            case 2:
                print("Buscar cita")
                Buscarcita(Buscarcita)
            case 3:
                print("Imprimir atencion")
                Imprimir(Imprimir)
            case 4:
                print("Salir")
                ciclo= Salir()
            case _:
                print("Opcion incorrecta:")
    except BaseException as error:
        print(f"Error:{error}")







