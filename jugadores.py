from utiles import generar_id, leer_texto, leer_int, imprimir_tabla, pausar
import equipos

# Lista de jugadores en memoria
jugadores = []

def crear_jugador():
    """Crea un nuevo jugador"""
    print("\n--- ALTA DE JUGADOR ---")
    
    # Mostrar equipos activos
    equipos_activos = []
    for equipo in equipos.equipos:
        if equipo["activo"]:
            equipos_activos.append([equipo["id"], equipo["nombre"]])
    
    if len(equipos_activos) == 0:
        print("No hay equipos activos. Crea un equipo primero.")
        pausar()
        return
    
    print("\nEquipos disponibles:")
    imprimir_tabla(equipos_activos, ["ID", "Nombre"])
    
    nombre = leer_texto("\nNombre del jugador: ")
    posicion = leer_texto("Posición: ")
    equipo_id = leer_int("ID del equipo: ", 1)
    
    # Validar que el equipo existe y está activo
    equipo = equipos.buscar_equipo_por_id_interno(equipo_id)
    
    if equipo is None:
        print("El equipo no existe.")
        pausar()
        return
    
    if not equipo["activo"]:
        print("El equipo no está activo.")
        pausar()
        return
    
    jugador = {
        "id": generar_id(),
        "nombre": nombre,
        "posicion": posicion,
        "equipo_id": equipo_id,
        "activo": True
    }
    
    jugadores.append(jugador)
    print(f"\nJugador '{nombre}' creado exitosamente con ID {jugador['id']}")
    pausar()

def listar_jugadores():
    """Lista todos los jugadores o los de un equipo específico"""
    print("\n--- LISTAR JUGADORES ---")
    print("1. Listar todos los jugadores")
    print("2. Listar jugadores de un equipo")
    
    opcion = leer_int("\nElige una opción: ", 1)
    
    lista_jugadores = []
    
    if opcion == 1:
        # Listar todos
        for jugador in jugadores:
            if jugador["activo"]:
                equipo = equipos.buscar_equipo_por_id_interno(jugador["equipo_id"])
                nombre_equipo = equipo["nombre"] if equipo else "Desconocido"
                lista_jugadores.append([
                    jugador["id"],
                    jugador["nombre"],
                    jugador["posicion"],
                    nombre_equipo
                ])
    elif opcion == 2:
        # Listar de un equipo
        equipo_id = leer_int("ID del equipo: ", 1)
        for jugador in jugadores:
            if jugador["activo"] and jugador["equipo_id"] == equipo_id:
                equipo = equipos.buscar_equipo_por_id_interno(jugador["equipo_id"])
                nombre_equipo = equipo["nombre"] if equipo else "Desconocido"
                lista_jugadores.append([
                    jugador["id"],
                    jugador["nombre"],
                    jugador["posicion"],
                    nombre_equipo
                ])
    else:
        print("Opción no válida.")
        pausar()
        return
    
    if len(lista_jugadores) == 0:
        print("\nNo hay jugadores para mostrar.")
    else:
        print()
        imprimir_tabla(lista_jugadores, ["ID", "Nombre", "Posición", "Equipo"])
    
    pausar()

def buscar_jugador_por_id():
    """Busca y muestra un jugador por su ID"""
    print("\n--- BUSCAR JUGADOR ---")
    id_buscar = leer_int("ID del jugador: ", 1)
    
    encontrado = False
    for jugador in jugadores:
        if jugador["id"] == id_buscar:
            encontrado = True
            equipo = equipos.buscar_equipo_por_id_interno(jugador["equipo_id"])
            nombre_equipo = equipo["nombre"] if equipo else "Desconocido"
            
            print("\n--- FICHA DEL JUGADOR ---")
            print(f"ID: {jugador['id']}")
            print(f"Nombre: {jugador['nombre']}")
            print(f"Posición: {jugador['posicion']}")
            print(f"Equipo: {nombre_equipo}")
            print(f"Activo: {'Sí' if jugador['activo'] else 'No'}")
    
    if not encontrado:
        print("Jugador no encontrado.")
    
    pausar()

def actualizar_jugador():
    """Actualiza los datos de un jugador"""
    print("\n--- ACTUALIZAR JUGADOR ---")
    id_actualizar = leer_int("ID del jugador a actualizar: ", 1)
    
    encontrado = False
    for jugador in jugadores:
        if jugador["id"] == id_actualizar:
            encontrado = True
            print(f"\nJugador actual: {jugador['nombre']} - {jugador['posicion']}")
            
            nuevo_nombre = leer_texto("Nuevo nombre: ")
            nueva_posicion = leer_texto("Nueva posición: ")
            nuevo_equipo_id = leer_int("Nuevo ID del equipo: ", 1)
            
            # Validar el nuevo equipo
            equipo = equipos.buscar_equipo_por_id_interno(nuevo_equipo_id)
            
            if equipo is None:
                print("El equipo no existe.")
                pausar()
                return
            
            if not equipo["activo"]:
                print("El equipo no está activo.")
                pausar()
                return
            
            jugador["nombre"] = nuevo_nombre
            jugador["posicion"] = nueva_posicion
            jugador["equipo_id"] = nuevo_equipo_id
            print("\nJugador actualizado exitosamente.")
    
    if not encontrado:
        print("Jugador no encontrado.")
    
    pausar()

def eliminar_jugador():
    """Elimina (desactiva) un jugador"""
    print("\n--- ELIMINAR JUGADOR ---")
    id_eliminar = leer_int("ID del jugador a eliminar: ", 1)
    
    encontrado = False
    for jugador in jugadores:
        if jugador["id"] == id_eliminar:
            encontrado = True
            jugador["activo"] = False
            print(f"\nJugador '{jugador['nombre']}' eliminado exitosamente.")
    
    if not encontrado:
        print("Jugador no encontrado.")
    
    pausar()

def menu_jugadores():
    """Menú del módulo de jugadores"""
    salir = False
    
    while not salir:
        print("\n" + "="*50)
        print("MÓDULO 2 - GESTIÓN DE JUGADORES")
        print("="*50)
        print("1. Alta de jugador")
        print("2. Listar jugadores")
        print("3. Buscar jugador por ID")
        print("4. Actualizar jugador")
        print("5. Eliminar jugador")
        print("6. Volver al menú principal")
        
        opcion = leer_int("\nElige una opción: ", 1)
        
        if opcion == 1:
            crear_jugador()
        elif opcion == 2:
            listar_jugadores()
        elif opcion == 3:
            buscar_jugador_por_id()
        elif opcion == 4:
            actualizar_jugador()
        elif opcion == 5:
            eliminar_jugador()
        elif opcion == 6:
            salir = True
        else:
            print("Opción no válida.")
            pausar()