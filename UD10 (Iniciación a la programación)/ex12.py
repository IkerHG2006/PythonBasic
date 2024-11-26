import os

ruta_directorio = "/home/cicles/AO/Prova"
ruta_archivo = os.path.join(ruta_directorio, "Ex12.txt")

os.makedirs(ruta_directorio, exist_ok=True)

with open(ruta_archivo, 'w') as archivo:
    archivo.write("Alumno1\nAlumno2\nAlumno3\n")

with open(ruta_archivo, 'a') as archivo:
    archivo.write("Profesor1\nProfesor2\n")

with open(ruta_archivo, 'r') as archivo:
    contenido = archivo.readlines()

print(contenido)