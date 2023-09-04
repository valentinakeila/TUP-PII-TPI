import libro as l
import cod_generator

from cod_generator import *

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)


def prestar_ejemplar_libro():
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


# 3) Registrar nuevo libro
# Si se adquieren nuevos libros los mismos deben registrarse. Agregar un libro y la
# cantidad de sus ejemplares adquiridos a la lista “libros”. Para el libro registrado se
# generará el código automáticamente y se informará el mismo con un resumen de los
# datos registrados.


def registrar_nuevo_libro():
    libroNuevo = nuevo_libro()
    libros.append(libroNuevo) 
    print("Codigo: ", libroNuevo['cod'] , libroNuevo['titulo'], "por", libroNuevo['autor'],"Stock: " , libroNuevo['cant_ej_stock'])
    return None


# 4) Eliminar ejemplar
# Si debe sacarse de circulación un ejemplar, debe actualizarse la cantidad de ejemplares
# adquiridos del libro. El bibliotecario debe ingresar el código del libro. Se valida que el
# mismo exista y se actualiza la cantidad de ejemplares adquiridos, en caso contrario se
# muestra error.

def eliminar_ejemplar_libro():
    buscar_codigo = input("\n Ingrese el codigo del libro a buscar: ")
    for busqueda in libros:
        if buscar_codigo == busqueda['cod'] and busqueda['cant_ej_stock'] > 0:
             busqueda['cant_ej_stock'] = 0
             libros.remove(busqueda)
             print("Se quito de stock el libro")

    return None

# 5) Mostrar ejemplares prestados
# De la lista “libros” mostrar la cantidad de ejemplares prestados de cada uno. En caso de
# no tener ningún ejemplar prestado mostrar un mensaje.

def ejemplares_prestados():
    for librosPrestados in libros:

        print(librosPrestados['titulo'])
        if librosPrestados['cant_ej_pr'] > 0:
            print("Libros prestados: ", librosPrestados['cant_ej_pr'])
        else:
            print("No hay ejemplares prestados de este libro")
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
    titulo = input("Ingrese el titulo del libro ")
    autor = input("Ingrese el autor ")
    stock = int(input("Ingrese cantidad de stock "))
    codigo = generar()
    libroNuevo = {'cod': codigo, 'cant_ej_stock': stock, 'cant_ej_pr': 0, "titulo": titulo, "autor": autor}
    return libroNuevo
