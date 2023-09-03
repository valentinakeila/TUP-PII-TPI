import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)


def ejemplares_prestados():
    encontrado = 0
    print("Estoy funcionando :)")
    buscar_codigo = input("\n Ingrese el codigo del libro a buscar: ")
    for busqueda in libros: #usamos la variable busqueda para buscar en libros y que la muestre abajo
        if buscar_codigo == busqueda['cod']:
             print("El código corresponde a:", busqueda['titulo'], "por", busqueda['autor'],"Stock: " , busqueda['cant_ej_stock'])
             encontrado = 1
             if busqueda['cant_ej_stock'] > 0:
                continuar = input("Quiere confirmar el prestamo? si / no ")
                if continuar == "si":
                 print("Prestamo hecho")
                 busqueda['cant_ej_pr'] = busqueda['cant_ej_pr'] + 1
                 busqueda['cant_ej_stock'] = busqueda['cant_ej_stock'] - 1
                 print("Cantidad de prestamos actuales en ese libro: ", busqueda['cant_ej_pr'])
                 print("Stock actual: ", busqueda['cant_ej_stock'])
                else:
                    print("Prestamo cancelado")
             elif busqueda['cant_ej_stock'] == 0:
                print("No queda stock suficiente para un prestamo")
            
            
    if encontrado == 0:
        print("Código incorrecto")
    
    return ""




def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    # completar
    return None


def eliminar_ejemplar_libro():
    # completar
    return None


def prestar_ejemplar_libro():
    # completar
    return None

# 2) Gestionar devolución
# El bibliotecario debe ingresar el código del libro. Se valida que el mismo exista y tenga
# ejemplares prestados, en caso contrario se muestra error.
# Para confirmar la devolución se muestra un mensaje y se actualiza la cantidad de
# ejemplares prestados.

def devolver_ejemplar_libro():
    encontrado = 0
    print("Estoy funcionando :)")
    buscar_codigo = input("\n Ingrese el codigo del libro a buscar: ")
    for busqueda in libros: #usamos la variable busqueda para buscar en libros y que la muestre abajo
        if buscar_codigo == busqueda['cod'] and busqueda['cant_ej_pr'] > 0:
            encontrado = 1
            print("Devolución realizada")
            busqueda['cant_ej_pr'] = busqueda['cant_ej_pr'] - 1
            busqueda['cant_ej_stock'] = busqueda['cant_ej_stock'] + 1
            print("Cantidad actual de ejemplares prestados: ", busqueda['cant_ej_pr'])
            print("Cantidad actual de stock: ", busqueda['cant_ej_stock'])


            
    if encontrado == 0:
        print("Código incorrecto o no hay ejemplares prestados")
    
    return ""


def nuevo_libro():
    # completar
    return None
