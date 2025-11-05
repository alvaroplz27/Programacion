from utiles import leer_int
import equipos
import jugadores
import calendario
import ranking

def main():
    "Función principal con el menú de la aplicación"
    print("="*50)
    print("LIGA DEPORTIVA AMATEUR")
    print("="*50)
    
    salir = False
    
    while not salir:
        print("\n" + "="*50)
        print("MENÚ PRINCIPAL")
        print("="*50)
        print("1. Gestión de equipos")
        print("2. Gestión de jugadores")
        print("3. Calendario de partidos")
        print("4. Resultados y clasificación")
        print("5. Salir")
        
        opcion = leer_int("\nElige una opción: ", 1)
        
        if opcion == 1:
            equipos.menu_equipos(jugadores.jugadores)
        elif opcion == 2:
            jugadores.menu_jugadores()
        elif opcion == 3:
            calendario.menu_calendario()
        elif opcion == 4:
            ranking.menu_ranking()
        elif opcion == 5:
            salir = True
            print("\n¡Hasta pronto!")
        else:
            print("Opcion no válida")

if __name__ == "__main__":
    main()