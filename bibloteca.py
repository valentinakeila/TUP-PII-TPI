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


def devolver_ejemplar_libro():
    # completar
    return None


def nuevo_libro():
    # completar
    return None
