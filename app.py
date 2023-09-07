# Trabajo Práctico I - Programación II
#Nicolas Cataldi
#Geraldine Corvalán
#Valentina Keila Garrido

import bibloteca
import os

from bibloteca import *

print("Bienvenido!")
respuesta = ''

def menu():
    print("1 - Gestionar Prestamo")
    print("2 - Gestionar Devolución")
    print("3 - Registrar nuevo libro")
    print("4 - Eliminar ejemplar")
    print("5 - Mostrar ejemplares prestados")
    print("6 - Salir")

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    #Comentamos el cls porque no funcionaba bien en nuestras terminales
    # os.system ("cls") #Limpiar pantalla
    #Pusimos las llmadas de las funciones en el menu
    if opt.isnumeric():
        if int(opt) == 1:
            
            prestar_ejemplar_libro()
        elif int(opt) == 2:
            devolver_ejemplar_libro()
           
        elif int(opt) == 3:
            registrar_nuevo_libro()
        elif int(opt) == 4:
            eliminar_ejemplar_libro()
        elif int(opt) == 5:
            ejemplares_prestados()
        elif int(opt) == 6:
            respuesta = "salir"
        else: print("Ingrese una opción válida")
    else: 
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para continuar....") # Pausa

print("Hasta luego!.")