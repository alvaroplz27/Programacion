from utiles import generar_id, leer_texto, leer_int, imprimir_tabla, pausar

# Lista de equipos en memoria
equipos = []

def crear_equipo():
    """Crea un nuevo equipo"""
    print("\n--- CREAR EQUIPO ---")
    nombre = leer_texto("Nombre del equipo: ")
    ciudad = leer_texto("Ciudad: ")
    
    equipo = {
        "id": generar_id(),
        "nombre": nombre,
        "ciudad": ciudad,
        "activo": True
    }
    
    equipos.append(equipo)
    print(f"\nEquipo '{nombre}' creado exitosamente con ID {equipo['id']}")
    pausar()

def listar_equipos():
    """Lista todos los equipos activos"""
    print("\n--- LISTA DE EQUIPOS ACTIVOS ---")
    
    equipos_activos = []
    for equipo in equipos:
        if equipo["activo"]:
            equipos_activos.append([
                equipo["id"],
                equipo["nombre"],
                equipo["ciudad"]
            ])
    
    if len(equipos_activos) == 0:
        print("No hay equipos activos.")
    else:
        imprimir_tabla(equipos_activos, ["ID", "Nombre", "Ciudad"])
    
    pausar()

def buscar_equipo_por_id():
    """Busca y muestra un equipo por su ID"""
    print("\n--- BUSCAR EQUIPO ---")
    id_buscar = leer_int("ID del equipo: ", 1)
    
    encontrado = False
    for equipo in equipos:
        if equipo["id"] == id_buscar:
            encontrado = True
            print("\n--- FICHA DEL EQUIPO ---")
            print(f"ID: {equipo['id']}")
            print(f"Nombre: {equipo['nombre']}")
            print(f"Ciudad: {equipo['ciudad']}")
            print(f"Activo: {'Sí' if equipo['activo'] else 'No'}")
    
    if not encontrado:
        print("Equipo no encontrado.")
    
    pausar()

def actualizar_equipo():
    """Actualiza los datos de un equipo"""
    print("\n--- ACTUALIZAR EQUIPO ---")
    id_actualizar = leer_int("ID del equipo a actualizar: ", 1)
    
    encontrado = False
    for equipo in equipos:
        if equipo["id"] == id_actualizar:
            encontrado = True
            print(f"\nEquipo actual: {equipo['nombre']} - {equipo['ciudad']}")
            nuevo_nombre = leer_texto("Nuevo nombre: ")
            nueva_ciudad = leer_texto("Nueva ciudad: ")
            
            equipo["nombre"] = nuevo_nombre
            equipo["ciudad"] = nueva_ciudad
            print("\nEquipo actualizado exitosamente.")
    
    if not encontrado:
        print("Equipo no encontrado.")
    
    pausar()

def eliminar_equipo(jugadores):
    """Elimina (desactiva) un equipo si no tiene jugadores"""
    print("\n--- ELIMINAR EQUIPO ---")
    id_eliminar = leer_int("ID del equipo a eliminar: ", 1)
    
    encontrado = False
    for equipo in equipos:
        if equipo["id"] == id_eliminar:
            encontrado = True
            
            # Verificar si tiene jugadores activos
            tiene_jugadores = False
            for jugador in jugadores:
                if jugador["equipo_id"] == id_eliminar and jugador["activo"]:
                    tiene_jugadores = True
            
            if tiene_jugadores:
                print("No se puede eliminar el equipo porque tiene jugadores activos.")
            else:
                equipo["activo"] = False
                print(f"\nEquipo '{equipo['nombre']}' eliminado exitosamente.")
    
    if not encontrado:
        print("Equipo no encontrado.")
    
    pausar()

def buscar_equipo_por_id_interno(id_equipo):
    """Busca un equipo por ID y lo devuelve (para uso interno)"""
    for equipo in equipos:
        if equipo["id"] == id_equipo:
            return equipo
    return None

def menu_equipos(jugadores):
    """Menú del módulo de equipos"""
    salir = False
    
    while not salir:
        print("\n" + "="*50)
        print("MÓDULO 1 - GESTIÓN DE EQUIPOS")
        print("="*50)
        print("1. Crear equipo")
        print("2. Listar equipos")
        print("3. Buscar equipo por ID")
        print("4. Actualizar equipo")
        print("5. Eliminar equipo")
        print("6. Volver al menú principal")
        
        opcion = leer_int("\nElige una opción: ", 1)
        
        if opcion == 1:
            crear_equipo()
        elif opcion == 2:
            listar_equipos()
        elif opcion == 3:
            buscar_equipo_por_id()
        elif opcion == 4:
            actualizar_equipo()
        elif opcion == 5:
            eliminar_equipo(jugadores)
        elif opcion == 6:
            salir = True
        else:
            print("Opción no válida.")
            pausar()