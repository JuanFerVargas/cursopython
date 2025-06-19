# Tabla de modos de apertura de archivos en Python:
# | Modo | Significado                                      |
# |------|--------------------------------------------------|
# | 'r'  | Leer (read). Abre el archivo solo para lectura.  |
# | 'w'  | Escribir (write). Sobrescribe o crea el archivo. |
# | 'a'  | Añadir (append). Escribe al final del archivo.   |
# | 'x'  | Crear. Falla si el archivo ya existe.            |
# | 'b'  | Binario (binary). Usado para archivos binarios.  |
# | 't'  | Texto (text). Modo por defecto, para texto.      |
# | '+'  | Actualizar (read/write). Lectura y escritura.    |
# Ejemplos: 'rb', 'w+', 'a+', etc.

import os

def crear_archivo(nombre, contenido=""):
    with open(nombre, 'w', encoding='utf-8') as f:
        f.write(contenido)

def leer_archivo(nombre):
    with open(nombre, 'r', encoding='utf-8') as f:
        return f.read()

def escribir_archivo(nombre, contenido):
    with open(nombre, 'w', encoding='utf-8') as f:
        f.write(contenido)

def agregar_a_archivo(nombre, contenido):
    with open(nombre, 'a', encoding='utf-8') as f:
        f.write(contenido)

def eliminar_archivo(nombre):
    if os.path.exists(nombre):
        os.remove(nombre)
    else:
        raise FileNotFoundError(f"El archivo {nombre} no existe.")

def renombrar_archivo(nombre_actual, nuevo_nombre):
    if os.path.exists(nombre_actual):
        os.rename(nombre_actual, nuevo_nombre)
    else:
        raise FileNotFoundError(f"El archivo {nombre_actual} no existe.")

def leer_lineas(nombre):
    with open(nombre, 'r', encoding='utf-8') as f:
        return f.readlines()

def escribir_lineas(nombre, lineas):
    with open(nombre, 'w', encoding='utf-8') as f:
        f.writelines(lineas)
