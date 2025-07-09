# Profundizando en el tipo str
# Las cadenas de texto son un tipo de dato fundamental en Python, utilizadas para representar texto.
import math
from Mi_Clase_16 import MiClase

# Concatenación automatica de cadenas
print('Concatenación automática de cadenas:')
variable='Adios'
mensaje = 'Hola ' 'Mundo ' + variable
mensaje += '!'
mensaje += ' Saludos a todos.'
# print(mensaje)

print('\n')
# help(str)  # Muestra la documentación del tipo str
# help(str.capitalize)  # Muestra la documentación del método capitalize

# help(math)  # Muestra la documentación del módulo math
# help(math.isinf)  # Muestra la documentación del módulo math

# help(MiClase)  # Muestra la documentación de MiClase
# print(MiClase.__doc__)  # Muestra la documentación de la clase MiClase
# print(MiClase.__init__.__doc__)  # Muestra la documentación del método __init__ de MiClase
# print(MiClase.metodo1.__doc__)  # Muestra la documentación del método metodo1 de MiClase
# print(MiClase.metodo2.__doc__)  # Muestra la documentación del método metodo2 de MiClase
# print(MiClase.metodo1)
# print(type(MiClase.metodo2))


mensaje1 = 'hola mundo'
mensaje2 = mensaje1.capitalize()  # Convierte la primera letra a mayúscula
mensaje3 = mensaje1.upper()  # Convierte todo el texto a mayúsculas

# print(f'\n{mensaje1} -> Id:{hex(id(mensaje1))} -> {type(mensaje1)}')
# print(f'{mensaje2} -> Id:{hex(id(mensaje2))} -> {type(mensaje2)}')
# print(f'{mensaje3} -> Id:{hex(id(mensaje3))} -> {type(mensaje3)}')


# help(str.join)  # Muestra la documentación de la función join

tupla = ('Python', 'es', 'genial')
mensaje4 = ' '.join(tupla)  # Une los elementos de la tupla
# print(f'\n{mensaje4} -> Id:{hex(id(mensaje4))} -> {type(mensaje4)}')

lista_cursos = ['Curso Python', 'Curso Java', 'Curso C++']
mensaje5 = ', '.join(lista_cursos)  # Une los elementos de la lista
# print(f'\n{mensaje5} -> Id:{hex(id(mensaje5))} -> {type(mensaje5)}')

cadena='HolaMundo'
mensaje6='.'.join(cadena)  # Une los caracteres de la cadena con un punto
# print(f'\n{mensaje6} -> Id:{hex(id(mensaje6))} -> {type(mensaje6)}')

diccionario = {'Python': 'PY', 'Java': 'JAR', 'C++': 'CPP'}  # Diccionario de lenguajes de programación
llaves = '-'.join(diccionario.keys())  # Une las claves del diccionario
valores = '-'.join(diccionario.values())  # Une los valores del diccionario
# print(f'\nLlaves: {llaves} -> Id:{hex(id(llaves))} -> {type(llaves)}')
# print(f'Valores: {valores} -> Id:{hex(id(valores))} -> {type(valores)}')

# help(str.split)  # Muestra la documentación de la función split
mensaje7 = 'Hola Mundo Python'
partes = mensaje7.split()  # Divide la cadena en partes usando espacios como separador
# print(f'\n{mensaje7} -> Id:{hex(id(mensaje7))} -> {type(mensaje7)}')
# print(f'Partes: {partes} -> Id:{hex(id(partes))} -> {type(partes)}')

mensaje8 = 'Hola,Mundo,Python'
partes2 = mensaje8.split(',')  # Divide la cadena en partes usando coma como separador
print(f'\n{mensaje8} -> Id:{hex(id(mensaje8))} -> {type(mensaje8)}')
print(f'Partes2: {partes2} -> Id:{hex(id(partes2))} -> {type(partes2)}')
