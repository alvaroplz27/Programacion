from tabulate import tabulate

# Variable global para generar IDs únicos
contador_id = 0

def generar_id():
    """Genera un ID único incrementando el contador"""
    global contador_id
    contador_id = contador_id + 1
    return contador_id

def leer_texto(mensaje):
    """Lee un texto no vacío del usuario"""
    texto = ""
    while texto == "":
        texto = input(mensaje).strip()
        if texto == "":
            print("El texto no puede estar vacío. Intenta de nuevo.")
    return texto

def leer_int(mensaje, minimo=None):
    """Lee un número entero del usuario"""
    numero = None
    while numero is None:
        entrada = input(mensaje)
        if entrada.isdigit():
            numero = int(entrada)
            if minimo is not None:
                if numero < minimo:
                    print(f"El número debe ser mayor o igual a {minimo}")
                    numero = None
        else:
            print("Debes introducir un número válido.")
    return numero

def imprimir_tabla(filas, columnas):
    """Imprime una tabla formateada"""
    if len(filas) == 0:
        print("No hay datos para mostrar.")
    else:
        print(tabulate(filas, headers=columnas, tablefmt="grid"))

def pausar():
    """Pausa la ejecución hasta que el usuario presione Enter"""
    input("\nPresiona Enter para continuar...")