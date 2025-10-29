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
