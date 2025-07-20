# Leer contenido online
from urllib.request import urlopen 


# Leer contenido online
with urlopen('https://www.globalmentoring.com.mx/recursos/GlobalMentoring.txt') as response:
    contenido = response.read().decode('utf-8')

# Contar concurrencias de palabras
print(f'Numero de ocurrencias de "Universidad": {contenido.count("Universidad")}')  # Contar la palabra 'Universidad'

print(contenido.upper())  # Convertir todo a mayúsculas
print(contenido.lower())  # Convertir todo a minúsculas
print(contenido.title())  # Convertir a formato título
print(contenido.capitalize())  # Convertir a mayúsculas la primera letra
print(contenido.strip())  # Eliminar espacios al inicio y al final
print(contenido.split())  # Dividir el contenido en palabras
print(f'Existe python?: ','python'.lower() in contenido.lower())  # Verificar si 'python' está en el contenido
print(f'Existe PYTHON?: ','python'.upper() in contenido.upper())  # Verificar si 'python' está en el contenido
print(f'Empieza con "En GlobalMentoring.com.mx": {contenido.startswith("En GlobalMentoring.com.mx")}') # Startwith
print(f'Termina con "Python": {contenido.endswith("Python")}') # Endwith
print('Hola Mundo'.lower().islower()) # Verificar si todo es minúscula
print('Hola Mundo'.upper().isupper()) # Verificar si todo es mayúscula
print('Hola Mundo'.title().istitle()) # Verificar si es formato título
print('Hola Mundo'.capitalize().istitle()) # Verificar si es formato título

# Alinear Cadenas

# Center
titulo = 'Sitio web de Global Mentoring'
print(len(titulo))
print(titulo.center(50, '*'))  # Centrar con asteriscos
print(titulo.center(50, '-'))  # Centrar con guiones
print(len(titulo.center(50, '*')))
print(titulo.center(len(titulo)+10, '*'))  # Centrar con espacios

print(titulo.ljust(50, '*'))  # Alinear a la izquierda
print(titulo.rjust(50, '*'))  # Alinear a la derecha

# Replace
print(titulo.replace(' ', '-'))  # Reemplazar espacios por guiones

# Eliminar caracteres al inicio y final de un string
titulo = '***Sitio web de Global Mentoring***'
print('Cadena Original:', titulo, len(titulo))
titulo = titulo.strip('*')  # Eliminar asteriscos al inicio y final
print('Cadena Modificada:', titulo, len(titulo))
titulo = '***Sitio web de Global Mentoring***'.lstrip('*')  # Eliminar asteriscos al inicio
print('Cadena Modificada:', titulo, len(titulo))
titulo = '***Sitio web de Global Mentoring***'.rstrip('*')  # Eliminar asteriscos al final
print('Cadena Modificada:', titulo, len(titulo))

titulo = ' *** Sitio web de Global Mentoring *** '.strip().strip('*').strip()  # Eliminar espacios y asteriscos al inicio y final
print('Cadena Modificada:', titulo, len(titulo))