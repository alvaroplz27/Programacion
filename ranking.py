from utiles import leer_int, imprimir_tabla, pausar
import equipos
import calendario

def registrar_resultado():
    """Registra el resultado de un partido pendiente"""
    print("\n--- REGISTRAR RESULTADO ---")
    
    # Mostrar partidos pendientes
    partidos_pendientes = []
    for partido in calendario.partidos:
        if not partido["jugado"]:
            local = equipos.buscar_equipo_por_id_interno(partido["local_id"])
            visitante = equipos.buscar_equipo_por_id_interno(partido["visitante_id"])
            
            nombre_local = local["nombre"] if local else "Desconocido"
            nombre_visitante = visitante["nombre"] if visitante else "Desconocido"
            
            partidos_pendientes.append([
                partido["id"],
                partido["jornada"],
                nombre_local,
                nombre_visitante,
                partido["fecha"]
            ])
    
    if len(partidos_pendientes) == 0:
        print("No hay partidos pendientes.")
        pausar()
        return
    
    print("\nPartidos pendientes:")
    imprimir_tabla(partidos_pendientes, ["ID", "Jornada", "Local", "Visitante", "Fecha"])
    
    id_partido = leer_int("\nID del partido: ", 1)
    
    encontrado = False
    for partido in calendario.partidos:
        if partido["id"] == id_partido:
            encontrado = True
            
            if partido["jugado"]:
                print("Este partido ya tiene resultado registrado.")
                pausar()
                return
            
            goles_local = leer_int("Goles del equipo local: ", 0)
            goles_visitante = leer_int("Goles del equipo visitante: ", 0)
            
            partido["resultado"] = (goles_local, goles_visitante)
            partido["jugado"] = True
            
            print("\nResultado registrado exitosamente.")
    
    if not encontrado:
        print("Partido no encontrado.")
    
    pausar()

def calcular_clasificacion():
    """Calcula y muestra la tabla de clasificación"""
    print("\n--- CLASIFICACIÓN ---")
    
    # Crear diccionario para almacenar estadísticas de cada equipo
    estadisticas = {}
    
    # Inicializar estadísticas para todos los equipos activos
    for equipo in equipos.equipos:
        if equipo["activo"]:
            estadisticas[equipo["id"]] = {
                "nombre": equipo["nombre"],
                "PJ": 0,
                "G": 0,
                "E": 0,
                "P": 0,
                "GF": 0,
                "GC": 0,
                "DG": 0,
                "PTS": 0
            }
    
    # Procesar todos los partidos jugados
    for partido in calendario.partidos:
        if partido["jugado"] and partido["resultado"] is not None:
            local_id = partido["local_id"]
            visitante_id = partido["visitante_id"]
            goles_local = partido["resultado"][0]
            goles_visitante = partido["resultado"][1]
            
            # Solo procesar si ambos equipos están en estadísticas
            if local_id in estadisticas and visitante_id in estadisticas:
                # Actualizar partidos jugados
                estadisticas[local_id]["PJ"] = estadisticas[local_id]["PJ"] + 1
                estadisticas[visitante_id]["PJ"] = estadisticas[visitante_id]["PJ"] + 1
                
                # Actualizar goles
                estadisticas[local_id]["GF"] = estadisticas[local_id]["GF"] + goles_local
                estadisticas[local_id]["GC"] = estadisticas[local_id]["GC"] + goles_visitante
                estadisticas[visitante_id]["GF"] = estadisticas[visitante_id]["GF"] + goles_visitante
                estadisticas[visitante_id]["GC"] = estadisticas[visitante_id]["GC"] + goles_local
                
                # Determinar resultado
                if goles_local > goles_visitante:
                    # Gana local
                    estadisticas[local_id]["G"] = estadisticas[local_id]["G"] + 1
                    estadisticas[local_id]["PTS"] = estadisticas[local_id]["PTS"] + 3
                    estadisticas[visitante_id]["P"] = estadisticas[visitante_id]["P"] + 1
                elif goles_local < goles_visitante:
                    # Gana visitante
                    estadisticas[visitante_id]["G"] = estadisticas[visitante_id]["G"] + 1
                    estadisticas[visitante_id]["PTS"] = estadisticas[visitante_id]["PTS"] + 3
                    estadisticas[local_id]["P"] = estadisticas[local_id]["P"] + 1
                else:
                    # Empate
                    estadisticas[local_id]["E"] = estadisticas[local_id]["E"] + 1
                    estadisticas[local_id]["PTS"] = estadisticas[local_id]["PTS"] + 1
                    estadisticas[visitante_id]["E"] = estadisticas[visitante_id]["E"] + 1
                    estadisticas[visitante_id]["PTS"] = estadisticas[visitante_id]["PTS"] + 1
    
    # Calcular diferencia de goles
    for equipo_id in estadisticas:
        estadisticas[equipo_id]["DG"] = estadisticas[equipo_id]["GF"] - estadisticas[equipo_id]["GC"]
    
    # Convertir a lista para ordenar
    lista_clasificacion = []
    for equipo_id in estadisticas:
        stats = estadisticas[equipo_id]
        lista_clasificacion.append([
            stats["nombre"],
            stats["PJ"],
            stats["G"],
            stats["E"],
            stats["P"],
            stats["GF"],
            stats["GC"],
            stats["DG"],
            stats["PTS"]
        ])
    
    # Ordenar por puntos de mayor a menor (ordenamiento de burbuja simple)
    n = len(lista_clasificacion)
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            # Comparar puntos (índice 8)
            if lista_clasificacion[j][8] < lista_clasificacion[j + 1][8]:
                # Intercambiar
                temp = lista_clasificacion[j]
                lista_clasificacion[j] = lista_clasificacion[j + 1]
                lista_clasificacion[j + 1] = temp
            j = j + 1
        i = i + 1
    
    if len(lista_clasificacion) == 0:
        print("No hay datos de clasificación.")
    else:
        print()
        imprimir_tabla(lista_clasificacion, ["Equipo", "PJ", "G", "E", "P", "GF", "GC", "DG", "PTS"])
    
    pausar()

def estadisticas_equipo():
    """Muestra estadísticas de un equipo específico"""
    print("\n--- ESTADÍSTICAS POR EQUIPO ---")
    
    # Mostrar equipos activos
    equipos_activos = []
    for equipo in equipos.equipos:
        if equipo["activo"]:
            equipos_activos.append([equipo["id"], equipo["nombre"]])
    
    if len(equipos_activos) == 0:
        print("No hay equipos activos.")
        pausar()
        return
    
    print("\nEquipos disponibles:")
    imprimir_tabla(equipos_activos, ["ID", "Nombre"])
    
    equipo_id = leer_int("\nID del equipo: ", 1)
    
    equipo = equipos.buscar_equipo_por_id_interno(equipo_id)
    
    if equipo is None or not equipo["activo"]:
        print("Equipo no encontrado o no activo.")
        pausar()
        return
    
    # Calcular estadísticas del equipo
    PJ = 0
    G = 0
    E = 0
    P = 0
    GF = 0
    GC = 0
    PTS = 0
    
    for partido in calendario.partidos:
        if partido["jugado"] and partido["resultado"] is not None:
            if partido["local_id"] == equipo_id or partido["visitante_id"] == equipo_id:
                PJ = PJ + 1
                
                if partido["local_id"] == equipo_id:
                    # El equipo juega como local
                    goles_favor = partido["resultado"][0]
                    goles_contra = partido["resultado"][1]
                else:
                    # El equipo juega como visitante
                    goles_favor = partido["resultado"][1]
                    goles_contra = partido["resultado"][0]
                
                GF = GF + goles_favor
                GC = GC + goles_contra
                
                if goles_favor > goles_contra:
                    G = G + 1
                    PTS = PTS + 3
                elif goles_favor < goles_contra:
                    P = P + 1
                else:
                    E = E + 1
                    PTS = PTS + 1
    
    DG = GF - GC
    
    print(f"\n--- ESTADÍSTICAS DE {equipo['nombre']} ---")
    print(f"Partidos jugados: {PJ}")
    print(f"Ganados: {G}")
    print(f"Empatados: {E}")
    print(f"Perdidos: {P}")
    print(f"Goles a favor: {GF}")
    print(f"Goles en contra: {GC}")
    print(f"Diferencia de goles: {DG}")
    print(f"Puntos: {PTS}")
    
    pausar()

def menu_ranking():
    """Menú del módulo de resultados y clasificación"""
    salir = False
    
    while not salir:
        print("\n" + "="*50)
        print("MÓDULO 4 - RESULTADOS Y CLASIFICACIÓN")
        print("="*50)
        print("1. Registrar resultado")
        print("2. Ver clasificación")
        print("3. Estadísticas por equipo")
        print("4. Volver al menú principal")
        
        opcion = leer_int("\nElige una opción: ", 1)
        
        if opcion == 1:
            registrar_resultado()
        elif opcion == 2:
            calcular_clasificacion()
        elif opcion == 3:
            estadisticas_equipo()
        elif opcion == 4:
            salir = True
        else:
            print("Opción no válida.")
            pausar()