# Leer contenido online
from urllib.request import urlopen 

with urlopen('https://www.globalmentoring.com.mx/recursos/GlobalMentoring.txt') as response:
    # contenido = response.read()
    contenido = response.read().decode('utf-8')
    print(contenido)

with open(nuevo_archivo := 'Curso_Python\\15_Profundizando_Python\\01_GlobalMentoring.txt', 'w', encoding='utf-8') as file:
    file.write(contenido)
print(f'Archivo guardado como: {nuevo_archivo}')
