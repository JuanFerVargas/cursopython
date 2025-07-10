# Leer contenido online
from urllib.request import urlopen 

palabras = []
# Leer contenido online
with urlopen('https://www.globalmentoring.com.mx/recursos/GlobalMentoring.txt') as response:
    for line in response:
        # Decodificar la línea y eliminar espacios en blanco
        palabras_por_linea = line.decode('utf-8').split()
        for palabra in palabras_por_linea:
            palabras.append(palabra)

# Guardar las palabras en un archivo
with open(nuevo_archivo := 'Curso_Python\\15_Profundizando_Python\\02_GlobalMentoring_Palabras.txt', 'w', encoding='utf-8') as file:
    for palabra in palabras:
        file.write(palabra + '\n')
print(f'Archivo guardado como: {nuevo_archivo}')