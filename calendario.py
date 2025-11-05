from utiles import generar_id, leer_texto, leer_int, imprimir_tabla, pausar
from datetime import datetime
import equipos

# Lista de partidos en memoria
partidos = []

def validar_fecha(fecha_str):
    """Valida que la fecha tenga formato YYYY-MM-DD"""
    try:
        datetime.strptime(fecha_str, "%Y-%m-%d")
        return True
    except:
        return False

def validar_hora(hora_str):
    """Valida que la hora tenga formato HH:MM"""
    try:
        datetime.strptime(hora_str, "%H:%M")
        return True
    except:
        return False

def crear_partido():
    """Crea un nuevo partido"""
    print("\n--- CREAR PARTIDO ---")
    
    # Mostrar equipos activos
    equipos_activos = []
    for equipo in equipos.equipos:
        if equipo["activo"]:
            equipos_activos.append([equipo["id"], equipo["nombre"]])
    
    if len(equipos_activos) < 2:
        print("Necesitas al menos 2 equipos activos para crear un partido.")
        pausar()
        return
    
    print("\nEquipos disponibles:")
    imprimir_tabla(equipos_activos, ["ID", "Nombre"])
    
    jornada = leer_int("\nJornada: ", 1)
    local_id = leer_int("ID equipo local: ", 1)
    visitante_id = leer_int("ID equipo visitante: ", 1)
    
    # Validaciones
    if local_id == visitante_id:
        print("El equipo local y visitante no pueden ser el mismo.")
        pausar()
        return
    
    equipo_local = equipos.buscar_equipo_por_id_interno(local_id)
    equipo_visitante = equipos.buscar_equipo_por_id_interno(visitante_id)
    
    if equipo_local is None or equipo_visitante is None:
        print("Uno de los equipos no existe.")
        pausar()
        return
    
    if not equipo_local["activo"] or not equipo_visitante["activo"]:
        print("Ambos equipos deben estar activos.")
        pausar()
        return
    
    # Validar fecha y hora
    fecha_valida = False
    while not fecha_valida:
        fecha = input("Fecha (YYYY-MM-DD): ")
        if validar_fecha(fecha):
            fecha_valida = True
        else:
            print("Formato de fecha inválido. Usa YYYY-MM-DD")
    
    hora_valida = False
    while not hora_valida:
        hora = input("Hora (HH:MM): ")
        if validar_hora(hora):
            hora_valida = True
        else:
            print("Formato de hora inválido. Usa HH:MM")
    
    # Verificar duplicado en la misma jornada
    for partido in partidos:
        if partido["jornada"] == jornada:
            mismo_enfrentamiento = (
                (partido["local_id"] == local_id and partido["visitante_id"] == visitante_id) or
                (partido["local_id"] == visitante_id and partido["visitante_id"] == local_id)
            )
            if mismo_enfrentamiento:
                print("Ya existe este enfrentamiento en la misma jornada.")
                pausar()
                return
    
    partido = {
        "id": generar_id(),
        "jornada": jornada,
        "local_id": local_id,
        "visitante_id": visitante_id,
        "fecha": fecha,
        "hora": hora,
        "jugado": False,
        "resultado": None
    }
    
    partidos.append(partido)
    print(f"\nPartido creado exitosamente con ID {partido['id']}")
    pausar()

def listar_partidos():
    """Lista todos los partidos o los de una jornada específica"""
    print("\n--- LISTAR PARTIDOS ---")
    print("1. Listar todos los partidos")
    print("2. Listar partidos de una jornada")
    
    opcion = leer_int("\nElige una opción: ", 1)
    
    lista_partidos = []
    
    if opcion == 1:
        # Listar todos
        for partido in partidos:
            local = equipos.buscar_equipo_por_id_interno(partido["local_id"])
            visitante = equipos.buscar_equipo_por_id_interno(partido["visitante_id"])
            
            nombre_local = local["nombre"] if local else "Desconocido"
            nombre_visitante = visitante["nombre"] if visitante else "Desconocido"
            
            estado = "Jugado" if partido["jugado"] else "Pendiente"
            resultado = ""
            if partido["resultado"] is not None:
                resultado = f"{partido['resultado'][0]} - {partido['resultado'][1]}"
            
            lista_partidos.append([
                partido["id"],
                partido["jornada"],
                nombre_local,
                nombre_visitante,
                partido["fecha"],
                partido["hora"],
                estado,
                resultado
            ])
    elif opcion == 2:
        # Listar de una jornada
        jornada = leer_int("Número de jornada: ", 1)
        for partido in partidos:
            if partido["jornada"] == jornada:
                local = equipos.buscar_equipo_por_id_interno(partido["local_id"])
                visitante = equipos.buscar_equipo_por_id_interno(partido["visitante_id"])
                
                nombre_local = local["nombre"] if local else "Desconocido"
                nombre_visitante = visitante["nombre"] if visitante else "Desconocido"
                
                estado = "Jugado" if partido["jugado"] else "Pendiente"
                resultado = ""
                if partido["resultado"] is not None:
                    resultado = f"{partido['resultado'][0]} - {partido['resultado'][1]}"
                
                lista_partidos.append([
                    partido["id"],
                    partido["jornada"],
                    nombre_local,
                    nombre_visitante,
                    partido["fecha"],
                    partido["hora"],
                    estado,
                    resultado
                ])
    else:
        print("Opción no válida.")
        pausar()
        return
    
    if len(lista_partidos) == 0:
        print("\nNo hay partidos para mostrar.")
    else:
        print()
        imprimir_tabla(lista_partidos, ["ID", "Jornada", "Local", "Visitante", "Fecha", "Hora", "Estado", "Resultado"])
    
    pausar()

def reprogramar_partido():
    """Reprograma la fecha y hora de un partido no jugado"""
    print("\n--- REPROGRAMAR PARTIDO ---")
    id_partido = leer_int("ID del partido a reprogramar: ", 1)
    
    encontrado = False
    for partido in partidos:
        if partido["id"] == id_partido:
            encontrado = True
            
            if partido["jugado"]:
                print("No se puede reprogramar un partido ya jugado.")
                pausar()
                return
            
            # Validar fecha y hora
            fecha_valida = False
            while not fecha_valida:
                nueva_fecha = input("Nueva fecha (YYYY-MM-DD): ")
                if validar_fecha(nueva_fecha):
                    fecha_valida = True
                else:
                    print("Formato de fecha inválido. Usa YYYY-MM-DD")
            
            hora_valida = False
            while not hora_valida:
                nueva_hora = input("Nueva hora (HH:MM): ")
                if validar_hora(nueva_hora):
                    hora_valida = True
                else:
                    print("Formato de hora inválido. Usa HH:MM")
            
            partido["fecha"] = nueva_fecha
            partido["hora"] = nueva_hora
            print("\nPartido reprogramado exitosamente.")
    
    if not encontrado:
        print("Partido no encontrado.")
    
    pausar()

def eliminar_partido():
    """Elimina un partido no jugado"""
    print("\n--- ELIMINAR PARTIDO ---")
    id_partido = leer_int("ID del partido a eliminar: ", 1)
    
    encontrado = False
    indice = 0
    indice_encontrado = -1
    
    for partido in partidos:
        if partido["id"] == id_partido:
            encontrado = True
            indice_encontrado = indice
            
            if partido["jugado"]:
                print("No se puede eliminar un partido ya jugado.")
                pausar()
                return
        indice = indice + 1
    
    if encontrado and indice_encontrado >= 0:
        partidos.pop(indice_encontrado)
        print("\nPartido eliminado exitosamente.")
    elif not encontrado:
        print("Partido no encontrado.")
    
    pausar()

def menu_calendario():
    """Menú del módulo de calendario"""
    salir = False
    
    while not salir:
        print("\n" + "="*50)
        print("MÓDULO 3 - CALENDARIO Y PARTIDOS")
        print("="*50)
        print("1. Crear partido")
        print("2. Listar partidos")
        print("3. Reprogramar partido")
        print("4. Eliminar partido")
        print("5. Volver al menú principal")
        
        opcion = leer_int("\nElige una opción: ", 1)
        
        if opcion == 1:
            crear_partido()
        elif opcion == 2:
            listar_partidos()
        elif opcion == 3:
            reprogramar_partido()
        elif opcion == 4:
            eliminar_partido()
        elif opcion == 5:
            salir = True
        else:
            print("Opción no válida.")
            pausar()