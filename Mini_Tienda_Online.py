# Definimos las variables
productos = [
    {"id": 1, "nombre": "Ratón", "precio": 12.5, "stock": 20, "activo": True}
]

opcion = ""

# Definimos el menú
while opcion != "7":
    print("\n--- Mini tienda online ---")
    print("1. Crear artículo")
    print("2. Listar artículos")
    print("3. Buscar artículo por id")
    print("4. Actualizar artículo")
    print("5. Eliminar artículo")
    print("6. Alternar activo/inactivo")
    print("7. Salir")

    opcion = input("Elige una opción (1-7): ")

    match opcion:
        case "1":
            id_nuevo = int(input("Escribe el id del nuevo artículo: "))
            existe = False
            for p in productos:
                if p["id"] == id_nuevo:
                    existe = True
            if existe:
                print("Este producto ya está creado.")
            else:
                nombre = input("Escribe el nombre del nuevo artículo: ")
                precio = float(input("Escribe el precio del nuevo artículo (>0): "))
                stock = int(input("Escribe cuántos quieres agregar (>=0): "))
                if precio > 0 and stock >= 0:
                    producto = {
                        "id": id_nuevo,
                        "nombre": nombre,
                        "precio": precio,
                        "stock": stock,
                        "activo": True
                    }
                    productos.append(producto)
                    print("Artículo creado correctamente.")
                else:
                    print("Precio o stock no válidos.")

        case "2":
            print("\n--- Lista de artículos ---")
            for p in productos:
                print(p)

        case "3":
            id_buscar = int(input("Escribe el id del artículo a buscar: "))
            encontrado = False
            for p in productos:
                if p["id"] == id_buscar:
                    print(p)
                    encontrado = True
            if not encontrado:
                print("No se encontró ese artículo.")

        case "4":
            id_actualizar = int(input("Escribe el id del artículo a actualizar: "))
            for p in productos:
                if p["id"] == id_actualizar:
                    p["nombre"] = input("Nuevo nombre: ")
                    p["precio"] = float(input("Nuevo precio: "))
                    p["stock"] = int(input("Nuevo stock: "))
                    print("Artículo actualizado correctamente.")
                    break
            else:
                print("No se encontró ese artículo.")

        case "5":
            id_eliminar = int(input("Escribe el id del artículo a eliminar: "))
            for p in productos:
                if p["id"] == id_eliminar:
                    productos.remove(p)
                    print("Artículo eliminado.")
                    break
            else:
                print("No se encontró ese artículo.")

        case "6":
            id_cambiar = int(input("Escribe el id del artículo a activar/desactivar: "))
            for p in productos:
                if p["id"] == id_cambiar:
                    p["activo"] = not p["activo"]
                    print("Estado cambiado.")
                    break
            else:
                print("No se encontró ese artículo.")

        case "7":
            print("Saliendo de la tienda...")

        case _:
            print("Opción no válida. Intenta de nuevo.")


