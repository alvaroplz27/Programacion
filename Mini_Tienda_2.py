#Definimos las variables que usaremos
productos = [
    {"id": 1, "nombre": "Ratón", "precio": 12.5, "stock": 20, "activo": True}
]

usuarios = [
    {"id": 1, "nombre": "Ana", "email": "ana@example.com", "activo": True}
]

opcion_principal = ""

#Menu principal
while opcion_principal != "3":
    print("\n--- MINI TIENDA ONLINE ---")
    print("1. Menú de artículos")
    print("2. Menú de usuarios")
    print("3. Salir")

    opcion_principal = input("Elige una opción (1-3): ")

#Menu de los articulos
    if opcion_principal == "1":
        opcion = ""
        while opcion != "7":
            print("\n--- MENÚ DE ARTÍCULOS ---")
            print("1. Crear artículo")
            print("2. Listar artículos")
            print("3. Buscar artículo por id")
            print("4. Actualizar artículo")
            print("5. Eliminar artículo")
            print("6. Alternar activo/inactivo")
            print("7. Volver")

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
                    print("Volviendo al menú principal...")

                case _:
                    print("Opción no válida. Intenta de nuevo.")

#Menu de los usuarios
    elif opcion_principal == "2":
        opcion_u = ""
        while opcion_u != "7":
            print("\n--- MENÚ DE USUARIOS ---")
            print("1. Crear usuario")
            print("2. Listar usuarios")
            print("3. Buscar usuario por id")
            print("4. Actualizar usuario")
            print("5. Eliminar usuario")
            print("6. Alternar activo/inactivo")
            print("7. Volver")

            opcion_u = input("Elige una opción (1-7): ")

            match opcion_u:
                case "1":
                    id_nuevo = int(input("Escribe el id del nuevo usuario: "))
                    existe = False
                    for u in usuarios:
                        if u["id"] == id_nuevo:
                            existe = True
                    if existe:
                        print("Este usuario ya está creado.")
                    else:
                        nombre = input("Escribe el nombre del nuevo usuario: ")
                        email = input("Escribe el email del nuevo usuario: ")
                        if "@" in email and "." in email:
                            usuario = {
                                "id": id_nuevo,
                                "nombre": nombre,
                                "email": email,
                                "activo": True
                            }
                            usuarios.append(usuario)
                            print("Usuario creado correctamente.")
                        else:
                            print("Email no válido.")

                case "2":
                    print("\n--- Lista de usuarios ---")
                    for u in usuarios:
                        print(u)

                case "3":
                    id_buscar = int(input("Escribe el id del usuario a buscar: "))
                    encontrado = False
                    for u in usuarios:
                        if u["id"] == id_buscar:
                            print(u)
                            encontrado = True
                    if not encontrado:
                        print("No se encontró ese usuario.")

                case "4":
                    id_actualizar = int(input("Escribe el id del usuario a actualizar: "))
                    for u in usuarios:
                        if u["id"] == id_actualizar:
                            u["nombre"] = input("Nuevo nombre: ")
                            u["email"] = input("Nuevo email: ")
                            print("Usuario actualizado correctamente.")
                            break
                    else:
                        print("No se encontró ese usuario.")

                case "5":
                    id_eliminar = int(input("Escribe el id del usuario a eliminar: "))
                    for u in usuarios:
                        if u["id"] == id_eliminar:
                            usuarios.remove(u)
                            print("Usuario eliminado.")
                            break
                    else:
                        print("No se encontró ese usuario.")

                case "6":
                    id_cambiar = int(input("Escribe el id del usuario a activar/desactivar: "))
                    for u in usuarios:
                        if u["id"] == id_cambiar:
                            u["activo"] = not u["activo"]
                            print("Estado cambiado.")
                            break
                    else:
                        print("No se encontró ese usuario.")

                case "7":
                    print("Volviendo al menú principal...")

                case _:
                    print("Opción no válida. Intenta de nuevo.")

    elif opcion_principal == "3":
        print("Saliendo de la tienda...")

    else:
        print("Opción no válida. Intenta de nuevo.")
