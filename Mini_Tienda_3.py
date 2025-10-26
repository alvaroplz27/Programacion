#Definimos las variables

productos = [
    {"id": 1, "nombre": "Ratón", "precio": 12.5, "stock": 20, "activo": True}
]

usuarios = [
    {"id": 1, "nombre": "Ana", "email": "ana@example.com", "activo": True}
]

ventas = []
carrito = []
usuario_activo = None

opcion_principal = ""

while opcion_principal != "4":
    print("\n--- MINI TIENDA ONLINE ---")
    print("1. Menú artículos")
    print("2. Menú usuarios")
    print("3. Menú ventas / carrito")
    print("4. Salir")

    opcion_principal = input("Elige una opción (1-4): ")

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
                    id_nuevo = int(input("Id del nuevo artículo: "))
                    existe = False
                    for p in productos:
                        if p["id"] == id_nuevo:
                            existe = True
                    if existe == True:
                        print("Ese id ya existe.")
                    else:
                        nombre = input("Nombre: ")
                        precio = float(input("Precio (>0): "))
                        stock = int(input("Stock (>=0): "))
                        if precio > 0 and stock >= 0:
                            producto = {"id": id_nuevo, "nombre": nombre, "precio": precio, "stock": stock, "activo": True}
                            productos.append(producto)
                            print("Artículo creado correctamente.")
                        else:
                            print("Datos incorrectos.")

                case "2":
                    for p in productos:
                        print(p)

                case "3":
                    id_buscar = int(input("Id del artículo a buscar: "))
                    encontrado = False
                    for p in productos:
                        if p["id"] == id_buscar:
                            print(p)
                            encontrado = True
                    if encontrado == False:
                        print("No se encontró ese artículo.")

                case "4":
                    id_act = int(input("Id del artículo a actualizar: "))
                    actualizado = False
                    for p in productos:
                        if p["id"] == id_act:
                            p["nombre"] = input("Nuevo nombre: ")
                            p["precio"] = float(input("Nuevo precio: "))
                            p["stock"] = int(input("Nuevo stock: "))
                            actualizado = True
                    if actualizado == True:
                        print("Artículo actualizado.")
                    else:
                        print("No se encontró ese artículo.")

                case "5":
                    id_eliminar = int(input("Id del artículo a eliminar: "))
                    nueva_lista = []
                    eliminado = False
                    for p in productos:
                        if p["id"] != id_eliminar:
                            nueva_lista.append(p)
                        else:
                            eliminado = True
                    productos = nueva_lista
                    if eliminado == True:
                        print("Artículo eliminado.")
                    else:
                        print("No se encontró ese artículo.")

                case "6":
                    id_cambiar = int(input("Id del artículo a cambiar estado: "))
                    cambiado = False
                    for p in productos:
                        if p["id"] == id_cambiar:
                            if p["activo"] == True:
                                p["activo"] = False
                            else:
                                p["activo"] = True
                            cambiado = True
                    if cambiado == True:
                        print("Estado cambiado.")
                    else:
                        print("No se encontró ese artículo.")

                case "7":
                    print("Volviendo al menú principal...")

                case _:
                    print("Opción no válida.")

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
                    id_nuevo = int(input("Id del nuevo usuario: "))
                    existe = False
                    for u in usuarios:
                        if u["id"] == id_nuevo:
                            existe = True
                    if existe == True:
                        print("Ese usuario ya existe.")
                    else:
                        nombre = input("Nombre: ")
                        email = input("Email: ")
                        if "@" in email and "." in email:
                            usuario = {"id": id_nuevo, "nombre": nombre, "email": email, "activo": True}
                            usuarios.append(usuario)
                            print("Usuario creado correctamente.")
                        else:
                            print("Email no válido.")

                case "2":
                    for u in usuarios:
                        print(u)

                case "3":
                    id_buscar = int(input("Id del usuario a buscar: "))
                    encontrado = False
                    for u in usuarios:
                        if u["id"] == id_buscar:
                            print(u)
                            encontrado = True
                    if encontrado == False:
                        print("No se encontró ese usuario.")

                case "4":
                    id_act = int(input("Id del usuario a actualizar: "))
                    actualizado = False
                    for u in usuarios:
                        if u["id"] == id_act:
                            u["nombre"] = input("Nuevo nombre: ")
                            u["email"] = input("Nuevo email: ")
                            actualizado = True
                    if actualizado == True:
                        print("Usuario actualizado.")
                    else:
                        print("No se encontró ese usuario.")

                case "5":
                    id_eliminar = int(input("Id del usuario a eliminar: "))
                    nueva_lista = []
                    eliminado = False
                    for u in usuarios:
                        if u["id"] != id_eliminar:
                            nueva_lista.append(u)
                        else:
                            eliminado = True
                    usuarios = nueva_lista
                    if eliminado == True:
                        print("Usuario eliminado.")
                    else:
                        print("No se encontró ese usuario.")

                case "6":
                    id_cambiar = int(input("Id del usuario a cambiar estado: "))
                    cambiado = False
                    for u in usuarios:
                        if u["id"] == id_cambiar:
                            if u["activo"] == True:
                                u["activo"] = False
                            else:
                                u["activo"] = True
                            cambiado = True
                    if cambiado == True:
                        print("Estado cambiado.")
                    else:
                        print("No se encontró ese usuario.")

                case "7":
                    print("Volviendo...")

                case _:
                    print("Opción no válida.")

#Menu de las ventas y el carrito
    elif opcion_principal == "3":
        opcion_v = ""
        while opcion_v != "8":
            print("\n--- MENÚ DE VENTAS / CARRITO ---")
            print("1. Seleccionar usuario activo")
            print("2. Añadir artículo al carrito")
            print("3. Quitar artículo del carrito")
            print("4. Ver carrito")
            print("5. Confirmar compra")
            print("6. Historial de ventas")
            print("7. Vaciar carrito")
            print("8. Volver")

            opcion_v = input("Elige una opción (1-8): ")

            match opcion_v:
                case "1":
                    id_usuario = int(input("Id del usuario activo: "))
                    existe = False
                    for u in usuarios:
                        if u["id"] == id_usuario and u["activo"] == True:
                            usuario_activo = id_usuario
                            existe = True
                    if existe == True:
                        print("Usuario seleccionado.")
                    else:
                        print("Usuario no válido o inactivo.")

                case "2":
                    if usuario_activo == None:
                        print("Selecciona un usuario activo primero.")
                    else:
                        id_art = int(input("Id del artículo: "))
                        cantidad = int(input("Cantidad: "))
                        encontrado = False
                        for p in productos:
                            if p["id"] == id_art and p["activo"] == True:
                                if cantidad > 0 and cantidad <= p["stock"]:
                                    existe = False
                                    for c in carrito:
                                        if c["id"] == id_art:
                                            c["cantidad"] = c["cantidad"] + cantidad
                                            existe = True
                                    if existe == False:
                                        carrito.append({"id": id_art, "cantidad": cantidad})
                                    print("Artículo añadido al carrito.")
                                else:
                                    print("Cantidad no válida.")
                                encontrado = True
                        if encontrado == False:
                            print("Artículo no encontrado o inactivo.")

                case "3":
                    id_quitar = int(input("Id del artículo a quitar: "))
                    nueva_lista = []
                    quitado = False
                    for c in carrito:
                        if c["id"] != id_quitar:
                            nueva_lista.append(c)
                        else:
                            quitado = True
                    carrito = nueva_lista
                    if quitado == True:
                        print("Artículo quitado del carrito.")
                    else:
                        print("No se encontró ese artículo en el carrito.")

                case "4":
                    total = 0
                    print("\n--- CARRITO ACTUAL ---")
                    for c in carrito:
                        for p in productos:
                            if c["id"] == p["id"]:
                                subtotal = p["precio"] * c["cantidad"]
                                print(p["nombre"], "x", c["cantidad"], "=", subtotal, "€")
                                total = total + subtotal
                    print("Total:", total, "€")

                case "5":
                    if usuario_activo == None:
                        print("Selecciona un usuario activo primero.")
                    else:
                        if len(carrito) == 0:
                            print("El carrito está vacío.")
                        else:
                            total = 0
                            items = []
                            todo_correcto = True
                            for c in carrito:
                                encontrado = False
                                for p in productos:
                                    if p["id"] == c["id"]:
                                        encontrado = True
                                        if p["stock"] >= c["cantidad"]:
                                            subtotal = p["precio"] * c["cantidad"]
                                            items.append((p["id"], c["cantidad"], p["precio"]))
                                            total = total + subtotal
                                        else:
                                            todo_correcto = False
                                            print("No hay suficiente stock de", p["nombre"])
                                if encontrado == False:
                                    todo_correcto = False
                                    print("Artículo no encontrado.")
                            if todo_correcto == True:
                                for c in carrito:
                                    for p in productos:
                                        if p["id"] == c["id"]:
                                            p["stock"] = p["stock"] - c["cantidad"]
                                id_venta = len(ventas) + 1
                                venta = {"id_venta": id_venta, "usuario_id": usuario_activo, "items": items, "total": total}
                                ventas.append(venta)
                                carrito = []
                                print("Compra confirmada correctamente. Total:", total, "€")

                case "6":
                    id_user = int(input("Id del usuario: "))
                    print("\n--- HISTORIAL DE VENTAS ---")
                    encontrado = False
                    for v in ventas:
                        if v["usuario_id"] == id_user:
                            print(v)
                            encontrado = True
                    if encontrado == False:
                        print("No hay ventas de ese usuario.")

                case "7":
                    carrito = []
                    print("Carrito vaciado.")

                case "8":
                    print("Volviendo al menú principal...")

                case _:
                    print("Opción no válida.")

    elif opcion_principal == "4":
        print("Saliendo de la tienda...")

    else:
        print("Opción no válida.")
