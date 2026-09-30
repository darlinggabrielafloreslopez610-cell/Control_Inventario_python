# ==========================================
# Control DE INVENTARIO UTILIZANDO LISTAS
# Programación con Estructura de Datos
# ==========================================

inventario = []


def agregar_producto():
    while True:
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad: "))

        producto = {
            "nombre": nombre,
            "cantidad": cantidad
        }

        inventario.append(producto)

        print("Producto agregado correctamente.")

        continuar = input("¿Desea agregar otro producto? (s/n): ")

        if continuar.lower() == "n":
            break



def mostrar_productos():
    if len(inventario) == 0:
        print("El inventario está vacío.")
        return

    print("\n===== INVENTARIO =====")

    for i, producto in enumerate(inventario, start=1):
        print(f"{i}. {producto['nombre']} - Cantidad: {producto['cantidad']}")


def buscar_producto():
    nombre = input("Ingrese el nombre del producto que desea buscar: ")

    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            print(f"Producto encontrado: {producto['nombre']}")
            print(f"Cantidad disponible: {producto['cantidad']}")
            return

    print("Producto no encontrado.")


def actualizar_cantidad():
    nombre = input("Ingrese el nombre del producto: ")

    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            producto["cantidad"] = nueva_cantidad

            print("Cantidad actualizada correctamente.")
            return

    print("Producto no encontrado.")


def eliminar_producto():
    nombre = input("Ingrese el nombre del producto que desea eliminar: ")

    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            inventario.remove(producto)
            print("Producto eliminado correctamente.")
            return

    print("Producto no encontrado.")


# ==========================================
# MENÚ PRINCIPAL
# ==========================================

while True:

    print("\n==============================")
    print("  Módulo De inventario ")
    print("==============================")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Actualizar cantidad")
    print("5. Eliminar producto")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto()

    elif opcion == "2":
        mostrar_productos()

    elif opcion == "3":
        buscar_producto()

    elif opcion == "4":
        actualizar_cantidad()

    elif opcion == "5":
        eliminar_producto()

    elif opcion == "6":
        print(" Módulo de inventario cerrado correctamente.")
        break

    else:
        print("Opción no válida.")