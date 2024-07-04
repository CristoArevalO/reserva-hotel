import csv
from datetime import date

with open('habitaciones.csv','w', newline = '')as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerows({[]})
date.now().strftime("%d-%m-%y %H:%M:%S")

def menu():
    print("menu de opciones ")
    print("1- reservar habitacion ")
    print("2- buscar habitacion ")
    print("3- ver estado ")
    print("4- ventas diarias ")
    print("5- guardar ")
    print("6- salir")

#
lista = []
total_reserva = 0
hotel_reserva = 0
def reservar_habitacion(lista):
    habitacion = int(input("en que habitacion desea reservar"))
    nombre = input("ingrese nombre con el que desea reservar ")
    apellido = input("ingrese apellido con el que desea rervar ")
    rut = input("ingrese con el rut que desea ingresar ")
    hora_entrada = input("ingrese hora de entrada ")
    hora_salida = input("ingrese hora de salida")
    for piso in lista:
        if piso[0] == habitacion:
            piso[0] = nombre            
            piso[0] = apellido
            piso[0] = rut
            piso[0] = hora_entrada
            piso[0] = hora_salida
    for pisos in lista:
        for habitacion in lista_piso:
            if habitacion[1] == habitacion:
                habitacion[1] = "reservada"
    with open('habitaciones.csv','w', newline = '')as archivo_csv:
        writer = csv.writer(archivo_csv)
        

def buscar_habitacion(lista):
    habitacion = int(input("que habitacion desea buscar "))
    for piso in lista:
        for habitacion in lista_piso:
            habitacion[0] == habitacion
            print(habitacion)

def ver_estado(lista):
    for piso in total_reserva:
        print(piso)


def guardar(lista:)
    with open('habitaciones.csv', "w", newline = '')as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerows


lista_piso = [a]
a = 40
for hotel in range(0,5):
    for habitacion in range(0,8):
        lista_piso.append(a)
        lista_piso.append("nombre")
        lista_piso.append("apellido")
        lista_piso.append("rut")
        lista_piso.append("fecha: hora de entrada")
        lista_piso.append("fecha: hora de salida")
        a = a + 1
hotel_reserva.append(lista_piso)
print(hotel_reserva)

    
import csv
ciclo = True
while(ciclo):
    opcion = int(input("ingrese la opcion: "))
    match opcion:
        case 1:
            print("desea reservar habitacion ")
            print(hotel_reserva)
        case 2:
            print("desea buscar habitacion ")
            print(habitacion)
        case 3:
            print("desea ver el estado ")
            print(lista_piso)
        case 4:
            print("desea ver las ventas diarias ")
        case 5:
            print("desea guardar la informacion ")    
        case 5:
            print("salir")    





















































while True:
    option = int(input("Elija una opción: \n 1)  \n 2)  \n 3)  \n 4)  \n"))
    if option == 1:
    