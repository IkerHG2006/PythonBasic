def leer_archivo(ruta):
    try:
        with open(ruta, 'r') as archivo:
            return archivo.readlines()
    except FileNotFoundError:
        return "Error: El archivo no existe."
    except Exception as e:
        return f"Error inesperado: {e}"

resultado17 = leer_archivo("archivo_inexistente.txt")
print(resultado17)