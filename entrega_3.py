#Definimos los articulos

articulos = []

#Creamos las funciones
def generar_id(lista):
    if len(lista) == 0:
        return 1
    maximo = 0
    for item in lista:
        if item["id"] > maximo:
            maximo = item["id"]
    return maximo + 1


def leer_int(mensaje, minimo):
    valido = False
    while valido == False:
        try:
            num = int(input(mensaje))
            if num >= minimo:
                return num
            print(f"Debe ser >= {minimo}")
        except:
            print("Número no válido")


def leer_float(mensaje, minimo):
    valido = False
    while valido == False:
        try:
            num = float(input(mensaje))
            if num >= minimo:
                return num
            print(f"Debe ser >= {minimo}")
        except:
            print("Número no válido")


def buscar_por_id(lista, id_buscar):
    for item in lista:
        if item["id"] == id_buscar:
            return item
    return None


#Gestion de los articulos
def crear_articulo():
    nombre = input("Nombre: ")
    precio = leer_float("Precio: ", 0.01)
    stock = leer_int("Stock: ", 0)
    articulos.append({
        "id": generar_id(articulos),
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "activo": True
    })
    print("Artículo creado.")


def listar_articulos():
    print("\n1 - Todos")
    print("2 - Activos")
    print("3 - Inactivos")
    op = leer_int("Opción: ", 1)
    for a in articulos:
        mostrar = op == 1 or (op == 2 and a["activo"]) or (op == 3 and not a["activo"])
        if mostrar:
            estado = "Activo" if a["activo"] else "Inactivo"
            print(f"ID:{a['id']} | {a['nombre']} | ${a['precio']} | Stock:{a['stock']} | {estado}")


def buscar_articulo():
    art = buscar_por_id(articulos, leer_int("ID: ", 1))
    if art:
        print(f"ID:{art['id']} | {art['nombre']} | ${art['precio']} | Stock:{art['stock']} | {'Activo' if art['activo'] else 'Inactivo'}")
    else:
        print("No encontrado")


def actualizar_articulo():
    art = buscar_por_id(articulos, leer_int("ID: ", 1))
    if art == None:
        print("No encontrado")
        return
    nombre = input("Nuevo nombre (Enter=mantener): ")
    if nombre != "":
        art["nombre"] = nombre
    if input("¿Cambiar precio? (s/n): ") == "s":
        art["precio"] = leer_float("Precio: ", 0.01)
    if input("¿Cambiar stock? (s/n): ") == "s":
        art["stock"] = leer_int("Stock: ", 0)
    print("Artículo actualizado.")


def eliminar_articulo():
    id_del = leer_int("ID: ", 1)
    pos = 0
    for a in articulos:
        if a["id"] == id_del:
            articulos.pop(pos)
            print("Artículo eliminado.")
            return
        pos = pos + 1
    print("No encontrado")


def alternar_articulo():
    art = buscar_por_id(articulos, leer_int("ID: ", 1))
    if art:
        art["activo"] = not art["activo"]
        print("Estado cambiado.")
    else:
        print("No encontrado")


#Menu de los articulos
def menu_articulos():
    sigue = True
    while sigue:
        print("\n=== MENÚ ARTÍCULOS ===")
        print("1 - Crear")
        print("2 - Listar")
        print("3 - Buscar")
        print("4 - Actualizar")
        print("5 - Eliminar")
        print("6 - Alternar activo")
        print("7 - Salir")
        op = leer_int("Opción: ", 1)
        if op == 1:
            crear_articulo()
        elif op == 2:
            listar_articulos()
        elif op == 3:
            buscar_articulo()
        elif op == 4:
            actualizar_articulo()
        elif op == 5:
            eliminar_articulo()
        elif op == 6:
            alternar_articulo()
        elif op == 7:
            sigue = False

menu_articulos()

#Definimos las variables
articulos = []
usuarios = []

#Funciones con las utilidades
def generar_id(lista):
    if len(lista) == 0:
        return 1
    maximo = 0
    for item in lista:
        if "id" in item and item["id"] > maximo:
            maximo = item["id"]
    return maximo + 1


def leer_int(mensaje, minimo):
    valido = False
    while valido == False:
        try:
            num = int(input(mensaje))
            if num >= minimo:
                return num
            print(f"Debe ser >= {minimo}")
        except:
            print("Número no válido")


def leer_float(mensaje, minimo):
    valido = False
    while valido == False:
        try:
            num = float(input(mensaje))
            if num >= minimo:
                return num
            print(f"Debe ser >= {minimo}")
        except:
            print("Número no válido")


def buscar_por_id(lista, id_buscar):
    for item in lista:
        if item["id"] == id_buscar:
            return item
    return None


#Creamos las funciones de los articulos
def crear_articulo():
    nombre = input("Nombre: ")
    precio = leer_float("Precio: ", 0.01)
    stock = leer_int("Stock: ", 0)
    articulos.append({
        "id": generar_id(articulos),
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "activo": True
    })
    print("Artículo creado.")


def listar_articulos():
    print("\n1 - Todos")
    print("2 - Activos")
    print("3 - Inactivos")
    op = leer_int("Opción: ", 1)
    for a in articulos:
        mostrar = op == 1 or (op == 2 and a["activo"]) or (op == 3 and not a["activo"])
        if mostrar:
            estado = "Activo" if a["activo"] else "Inactivo"
            print(f"ID:{a['id']} | {a['nombre']} | ${a['precio']} | Stock:{a['stock']} | {estado}")


def buscar_articulo():
    art = buscar_por_id(articulos, leer_int("ID: ", 1))
    if art:
        print(f"ID:{art['id']} | {art['nombre']} | ${art['precio']} | Stock:{art['stock']} | {'Activo' if art['activo'] else 'Inactivo'}")
    else:
        print("No encontrado")


def actualizar_articulo():
    art = buscar_por_id(articulos, leer_int("ID: ", 1))
    if art == None:
        print("No encontrado")
        return
    nombre = input("Nuevo nombre (Enter=mantener): ")
    if nombre != "":
        art["nombre"] = nombre
    if input("¿Cambiar precio? (s/n): ") == "s":
        art["precio"] = leer_float("Precio: ", 0.01)
    if input("¿Cambiar stock? (s/n): ") == "s":
        art["stock"] = leer_int("Stock: ", 0)
    print("Artículo actualizado.")


def eliminar_articulo():
    id_del = leer_int("ID: ", 1)
    pos = 0
    for a in articulos:
        if a["id"] == id_del:
            articulos.pop(pos)
            print("Artículo eliminado.")
            return
        pos = pos + 1
    print("No encontrado")


def alternar_articulo():
    art = buscar_por_id(articulos, leer_int("ID: ", 1))
    if art:
        art["activo"] = not art["activo"]
        print("Estado cambiado.")
    else:
        print("No encontrado")


#Definimos las funciones de los usuarios
def crear_usuario():
    nombre = input("Nombre: ")
    email = ""
    while "@" not in email or "." not in email:
        email = input("Email: ")
        if "@" not in email or "." not in email:
            print("Email debe tener '@' y '.'")
    usuarios.append({
        "id": generar_id(usuarios),
        "nombre": nombre,
        "email": email,
        "activo": True
    })
    print("Usuario creado.")


def listar_usuarios():
    print("\n1 - Todos")
    print("2 - Activos")
    print("3 - Inactivos")
    op = leer_int("Opción: ", 1)
    for u in usuarios:
        mostrar = op == 1 or (op == 2 and u["activo"]) or (op == 3 and not u["activo"])
        if mostrar:
            estado = "Activo" if u["activo"] else "Inactivo"
            print(f"ID:{u['id']} | {u['nombre']} | {u['email']} | {estado}")


def buscar_usuario():
    usr = buscar_por_id(usuarios, leer_int("ID: ", 1))
    if usr:
        print(f"ID:{usr['id']} | {usr['nombre']} | {usr['email']} | {'Activo' if usr['activo'] else 'Inactivo'}")
    else:
        print("No encontrado")


def actualizar_usuario():
    usr = buscar_por_id(usuarios, leer_int("ID: ", 1))
    if usr == None:
        print("No encontrado")
        return
    nombre = input("Nuevo nombre (Enter=mantener): ")
    if nombre != "":
        usr["nombre"] = nombre
    if input("¿Cambiar email? (s/n): ") == "s":
        email = ""
        while "@" not in email or "." not in email:
            email = input("Email: ")
            if "@" not in email or "." not in email:
                print("Email debe tener '@' y '.'")
        usr["email"] = email
    print("Usuario actualizado.")


def eliminar_usuario():
    id_del = leer_int("ID: ", 1)
    pos = 0
    for u in usuarios:
        if u["id"] == id_del:
            usuarios.pop(pos)
            print("Usuario eliminado.")
            return
        pos = pos + 1
    print("No encontrado")


def alternar_usuario():
    usr = buscar_por_id(usuarios, leer_int("ID: ", 1))
    if usr:
        usr["activo"] = not usr["activo"]
        print("Estado cambiado.")
    else:
        print("No encontrado")


#Menus de los articulos y de los usuarios
def menu_articulos():
    sigue = True
    while sigue:
        print("\n=== MENÚ ARTÍCULOS ===")
        print("1 - Crear")
        print("2 - Listar")
        print("3 - Buscar")
        print("4 - Actualizar")
        print("5 - Eliminar")
        print("6 - Alternar activo")
        print("7 - Volver")
        op = leer_int("Opción: ", 1)
        if op == 1:
            crear_articulo()
        elif op == 2:
            listar_articulos()
        elif op == 3:
            buscar_articulo()
        elif op == 4:
            actualizar_articulo()
        elif op == 5:
            eliminar_articulo()
        elif op == 6:
            alternar_articulo()
        elif op == 7:
            sigue = False


def menu_usuarios():
    sigue = True
    while sigue:
        print("\n=== MENÚ USUARIOS ===")
        print("1 - Crear")
        print("2 - Listar")
        print("3 - Buscar")
        print("4 - Actualizar")
        print("5 - Eliminar")
        print("6 - Alternar activo")
        print("7 - Volver")
        op = leer_int("Opción: ", 1)
        if op == 1:
            crear_usuario()
        elif op == 2:
            listar_usuarios()
        elif op == 3:
            buscar_usuario()
        elif op == 4:
            actualizar_usuario()
        elif op == 5:
            eliminar_usuario()
        elif op == 6:
            alternar_usuario()
        elif op == 7:
            sigue = False


#Menu principal junto
sigue = True
while sigue:
    print("\n=== MINI TIENDA ONLINE ===")
    print("1 - Artículos")
    print("2 - Usuarios")
    print("3 - Salir")
    op = leer_int("Opción: ", 1)
    if op == 1:
        menu_articulos()
    elif op == 2:
        menu_usuarios()
    elif op == 3:
        sigue = False
        print("Adiós")

#Entrega 3
#Definimos las variables

ventas = []
carrito = []
usuario_activo = None


def seleccionar_usuario():
    global usuario_activo
    listar_usuarios()
    usr = buscar_por_id(usuarios, leer_int("ID usuario: ", 1))
    if usr and usr["activo"]:
        usuario_activo = usr["id"]
        print(f"Usuario {usr['nombre']} seleccionado.")
    else:
        print("Usuario no válido.")


def anadir_carrito():
    if usuario_activo == None:
        print("Selecciona usuario primero.")
        return
    listar_articulos()
    art = buscar_por_id(articulos, leer_int("ID artículo: ", 1))
    if art == None or not art["activo"]:
        print("Artículo no disponible.")
        return
    cant = leer_int(f"Cantidad (máx {art['stock']}): ", 1)
    if cant > art["stock"]:
        print("Stock insuficiente.")
        return
    pos = None
    i = 0
    for item in carrito:
        if item[0] == art["id"]:
            pos = i
        i = i + 1
    if pos == None:
        carrito.append((art["id"], cant))
    else:
        nueva = carrito[pos][1] + cant
        if nueva > art["stock"]:
            print("Stock insuficiente.")
            return
        carrito[pos] = (art["id"], nueva)
    print("Añadido al carrito.")


def quitar_carrito():
    if len(carrito) == 0:
        print("Carrito vacío.")
        return
    id_art = leer_int("ID artículo: ", 1)
    pos = 0
    for item in carrito:
        if item[0] == id_art:
            carrito.pop(pos)
            print("Artículo quitado.")
            return
        pos = pos + 1
    print("No está en el carrito.")


def ver_carrito():
    if len(carrito) == 0:
        print("Carrito vacío.")
        return
    total = 0
    for item in carrito:
        art = buscar_por_id(articulos, item[0])
        if art:
            sub = art["precio"] * item[1]
            total = total + sub
            print(f"{art['nombre']} x{item[1]} = ${sub}")
    print(f"TOTAL: ${total}")


def confirmar_compra():
    if usuario_activo == None or len(carrito) == 0:
        print("Necesitas usuario y carrito con artículos.")
        return
    ver_carrito()
    if input("¿Confirmar compra? (s/n): ") != "s":
        print("Cancelado.")
        return
    items = []
    total = 0
    for item in carrito:
        art = buscar_por_id(articulos, item[0])
        if art == None or not art["activo"] or art["stock"] < item[1]:
            print("Error: verifica stock.")
            return
        art["stock"] -= item[1]
        items.append((art["id"], item[1], art["precio"]))
        total += art["precio"] * item[1]
    ventas.append({
        "id_venta": generar_id(ventas),
        "usuario_id": usuario_activo,
        "items": items,
        "total": total
    })
    carrito.clear()
    print("Compra confirmada.")


def historial_ventas():
    usr = buscar_por_id(usuarios, leer_int("ID usuario: ", 1))
    if usr == None:
        print("Usuario no encontrado.")
        return
    print(f"\nHistorial de ventas de {usr['nombre']}:")
    for v in ventas:
        if v["usuario_id"] == usr["id"]:
            print(f"\nVenta #{v['id_venta']} - Total: ${v['total']}")
            for item in v["items"]:
                art = buscar_por_id(articulos, item[0])
                nombre = art["nombre"] if art else f"ID{item[0]}"
                print(f"  {nombre} x{item[1]} a ${item[2]}")


#Menu para las ventas
def menu_ventas():
    sigue = True
    while sigue:
        print("\n=== MENÚ VENTAS ===")
        print("1 - Seleccionar usuario")
        print("2 - Añadir al carrito")
        print("3 - Quitar del carrito")
        print("4 - Ver carrito")
        print("5 - Confirmar compra")
        print("6 - Historial por usuario")
        print("7 - Vaciar carrito")
        print("8 - Volver")
        op = leer_int("Opción: ", 1)
        if op == 1:
            seleccionar_usuario()
        elif op == 2:
            anadir_carrito()
        elif op == 3:
            quitar_carrito()
        elif op == 4:
            ver_carrito()
        elif op == 5:
            confirmar_compra()
        elif op == 6:
            historial_ventas()
        elif op == 7:
            carrito.clear()
            print("Carrito vaciado.")
        elif op == 8:
            sigue = False


#Menu principal con todo
def menu_principal():
    sigue = True
    while sigue:
        print("\n=== MINI TIENDA ONLINE ===")
        print("1 - Artículos")
        print("2 - Usuarios")
        print("3 - Ventas")
        print("4 - Salir")
        op = leer_int("Opción: ", 1)
        if op == 1:
            menu_articulos()
        elif op == 2:
            menu_usuarios()
        elif op == 3:
            menu_ventas()
        elif op == 4:
            sigue = False
            print("Adiós")

menu_principal()
