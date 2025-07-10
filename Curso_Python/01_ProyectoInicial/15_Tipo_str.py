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

# print('\n')
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
# print(f'\n{mensaje8} -> Id:{hex(id(mensaje8))} -> {type(mensaje8)}')
# print(f'Partes2: {partes2} -> Id:{hex(id(partes2))} -> {type(partes2)}')


# Dar formato a un string
nombre = 'Juan'
edad = 30
mensaje_con_formato ='Hola, mi nombre es %s y tengo %d años.'%(nombre,edad)  # Usando el operador % para formatear
# print(f'\n{mensaje_con_formato} -> Id:{hex(id(mensaje_con_formato))} -> {type(mensaje_con_formato)}')

mensaje_con_formato2 = 'Hola, mi nombre es {} y tengo {} años.'.format(nombre, edad)  # Usando el método format
# print(f'{mensaje_con_formato2} -> Id:{hex(id(mensaje_con_formato2))} -> {type(mensaje_con_formato2)}')

persona=('Karla', 'Gomez',5000.00)
mensaje_con_formato3 = 'Hola, mi nombre es %s %s y mi salario es $%.2f.'%(persona) 
# print(f'{mensaje_con_formato3} -> Id:{hex(id(mensaje_con_formato3))} -> {type(mensaje_con_formato3)}')

mensaje_con_formato4  = 'Hola, mi nombre es %s %s y mi salario es $%.2f.' # Usando el operador % para formatear con una tupla
# print(mensaje_con_formato4%persona)

mensaje_con_formato5 = 'Hola, mi nombre es {} {} y mi salario es ${:.2f}.'.format(*persona)  # Usando el método format con una tupla
# print(f'{mensaje_con_formato5} -> Id:{hex(id(mensaje_con_formato5))} -> {type(mensaje_con_formato5)}')

mensaje_con_formato6 = 'Hola, mi nombre es {0} {1} y mi salario es ${2:.2f}.'.format(*persona)  # Usando el método format con una tupla
# print(f'{mensaje_con_formato6} -> Id:{hex(id(mensaje_con_formato6))} -> {type(mensaje_con_formato6)}')

mensaje_con_formato7 = 'Hola, mi nombre es {n} {e} y mi salario es ${s:.2f}.'.format(n=persona[0], e=persona[1], s=persona[2])  # Usando el método format con una tupla
# print(f'{mensaje_con_formato7} -> Id:{hex(id(mensaje_con_formato7))} -> {type(mensaje_con_formato7)}')

diccionario_persona = {'nombre': 'Carlos', 'apellido': 'Perez', 'salario': 6000.00}
mensaje_con_formato8 = 'Hola, mi nombre es {persona[nombre]} {persona[apellido]} y mi salario es ${persona[salario]:.2f}.'.format(persona=diccionario_persona)  # Usando el método format con un diccionario
# print(f'{mensaje_con_formato8} -> Id:{hex(id(mensaje_con_formato8))} -> {type(mensaje_con_formato8)}')

# Usando f-strings (Python 3.6+)
# Las f-strings son una forma más moderna y legible de formatear cadenas en Python.
# Permiten insertar expresiones directamente dentro de las cadenas usando llaves {}.
# Formato Sugerido:

nombre = 'Juan'
edad = 30
sueldo= 5000.00
mensaje_con_formato9 = f'Hola, mi nombre es {nombre} y tengo {edad} años. Mi sueldo es ${sueldo:.2f}.'  # Usando f-strings (Python 3.6+)
# print(f'{mensaje_con_formato9} -> Id:{hex(id(mensaje_con_formato9))} -> {type(mensaje_con_formato9)}')

# Metodo Print
# print(nombre, edad, sueldo, sep=' - ', end='.\n')  # Imprime variables separadas por ' - ' y termina con un punto y salto de línea


# Multiplicación de cadenas
mensaje10 = 'Hola ' * 3  # Repite la cadena 3 veces
# print(f'\n{mensaje10} -> Id:{hex(id(mensaje10))} -> {type(mensaje10)}')

# Multiplicación de tuplas
tupla_repetida = ('Hola',10) * 3
# print(f'Tupla repetida: {tupla_repetida} -> Id:{hex(id(tupla_repetida))} -> {type(tupla_repetida)}')

# Multiplicación de listas
lista_repetida = ['Hola', 10] * 3
# print(f'Lista repetida: {lista_repetida} -> Id:{hex(id(lista_repetida))} -> {type(lista_repetida)}')


# Caracteres de escape
mensaje11 = 'Hola\nMundo'  # \n es un carácter de escape para nueva línea
# print(f'\n{mensaje11} -> Id:{hex(id(mensaje11))} -> {type(mensaje11)}')

mensaje12 = 'Hola\tMundo'  # \t es un carácter de escape para tabulación
# print(f'{mensaje12} -> Id:{hex(id(mensaje12))} -> {type(mensaje12)}')

mensaje13 = 'Hola\\Mundo'  # \\ es un carácter de escape para barra invertida
# print(f'{mensaje13} -> Id:{hex(id(mensaje13))} -> {type(mensaje13)}')

mensaje14 = 'Hola\'Mundo'  # \' es un carácter de escape para comilla simple
# print(f'{mensaje14} -> Id:{hex(id(mensaje14))} -> {type(mensaje14)}')

mensaje15 = 'Hola\"Mundo'  # \" es un carácter de escape para comilla doble
# print(f'{mensaje15} -> Id:{hex(id(mensaje15))} -> {type(mensaje15)}')

mensaje16 = 'Hola\bMundo'  # \b es un carácter de escape para retroceso
# print(f'{mensaje16} -> Id:{hex(id(mensaje16))} -> {type(mensaje16)}')

mensaje17 = 'Hola\rMundo'  # \r es un carácter de escape para retorno de carro
# print(f'{mensaje17} -> Id:{hex(id(mensaje17))} -> {type(mensaje17)}')

mensaje18 = 'Hola\vMundo\v'  # \v es un carácter de escape para salto de línea vertical
# print(f'{mensaje18} -> Id:{hex(id(mensaje18))} -> {type(mensaje18)}')

mensaje19 = 'Hola\x48\x65\x6c\x6c\x6f'  # \x es un carácter de escape para caracteres hexadecimales
# print(f'{mensaje19} -> Id:{hex(id(mensaje19))} -> {type(mensaje19)}')

mensaje20 = 'Hola\u0048\u0065\u006c\u006c\u006f'  # \u es un carácter de escape para caracteres Unicode
# print(f'{mensaje20} -> Id:{hex(id(mensaje20))} -> {type(mensaje20)}')

mensaje21 = 'Hola\N{LATIN CAPITAL LETTER H}\N{LATIN SMALL LETTER E}\N{LATIN SMALL LETTER L}\N{LATIN SMALL LETTER L}\N{LATIN SMALL LETTER O}'  # \N es un carácter de escape para caracteres Unicode con nombre
# print(f'{mensaje21} -> Id:{hex(id(mensaje21))} -> {type(mensaje21)}')

mensaje22 = r'Hola\nMundo'  # r'' crea una cadena sin procesar, los caracteres de escape no se interpretan
# print(f'{mensaje22} -> Id:{hex(id(mensaje22))} -> {type(mensaje22)}')


# Caracteres de escape Unicode
# Los caracteres de escape Unicode permiten representar caracteres especiales y símbolos en cadenas de texto.
# Estos caracteres se representan mediante secuencias de escape que comienzan con \u o \U.
# \u se utiliza para caracteres Unicode de 16 bits, mientras que \U se utiliza para caracteres Unicode de 32 bits.
# Ejemplos de caracteres de escape Unicode
# \u es un carácter de escape para caracteres Unicode de 16 bits
# \U es un carácter de escape para caracteres Unicode de 32 bits

mensaje23 = 'Hola\u0020Mundo' # \u0020 es un carácter de escape para espacio
# print(f'{mensaje23} -> Id:{hex(id(mensaje23))} -> {type(mensaje23)}')

mensaje24 = 'Hola\U0001F923 Mundo'  # \U es un carácter de escape para caracteres Unicode de 32 bits
# print(f'{mensaje24} -> Id:{hex(id(mensaje24))} -> {type(mensaje24)}')

mensaje25 = 'Hola\U0000270C  Mundo'  # \U es un carácter de escape para caracteres Unicode de 32 bits
# print(f'{mensaje25} -> Id:{hex(id(mensaje25))} -> {type(mensaje25)}')

# Caracteres Ascii
mensaje26 = 'Hola Mundo'  # Cadena de texto normal
mensaje27 = 'Hola Mundo'.encode('ascii')  # Codifica la cadena en ASCII
# print(f'{mensaje26} -> Id:{hex(id(mensaje26))} -> {type(mensaje26)}')
# print(f'{mensaje27} -> Id:{hex(id(mensaje27))} -> {type(mensaje27)}')

mensaje28 = chr(72) + chr(111) + chr(108) + chr(97) + chr(32) + chr(77) + chr(117) + chr(110) + chr(100) + chr(111)   # Construye la cadena "Hola Mundo" usando caracteres ASCII
# print(f'{mensaje28} -> Id:{hex(id(mensaje28))} -> {type(mensaje28)}')

# Caracteres usando bytes
# Los bytes son una secuencia inmutable de enteros en el rango de 0 a 255.
# Se utilizan para representar datos binarios y son útiles para trabajar con archivos, redes y otros datos que no son texto.
# Las cadenas de bytes se crean utilizando el prefijo b''.
# Las cadenas de bytes son útiles para trabajar con datos binarios y se diferencian de las cadenas de texto normales.
# Las cadenas de bytes son inmutables, lo que significa que no se pueden modificar una vez creadas.
# Las cadenas de bytes se pueden crear utilizando el prefijo b''.
# Ejemplo de cadena de bytes

mensaje29 = b'Hola Mundo'  # Cadena de bytes
# print(f'{mensaje29} -> Id:{hex(id(mensaje29))} -> {type(mensaje29)}')
# print(mensaje29[0])  # Acceso al primer byte
# print(mensaje29[0:4])  # Acceso a un rango de bytes
# print(chr(mensaje29[0]))  # Conversión del primer byte a carácter
# Los bytes son inmutables, por lo que no se pueden modificar directamente.
# mensaje29[0] = 72  # Esto generaría un error porque los bytes

lista_caracteres=mensaje29.split()  # Convierte la cadena de bytes en una lista de bytes
# print(f'{lista_caracteres} -> Id:{hex(id(lista_caracteres))} -> {type(lista_caracteres)}')

lista_caracteres=mensaje29.decode('utf-8')  # Decodifica la cadena de bytes a una cadena de texto
# print(f'{lista_caracteres.split()} -> Id:{hex(id(lista_caracteres))} -> {type(lista_caracteres)}')

# Convertir de String a Bytes
# Las cadenas de texto se pueden convertir a bytes utilizando el método encode() de la clase str.
# Este método toma un argumento opcional que especifica la codificación a utilizar (por defecto
# es 'utf-8').
# La codificación 'utf-8' es la más común y admite una amplia gama de caracteres.
# La codificación 'ascii' es una codificación más limitada que solo admite caracteres ASCII.
# Ejemplo de conversión de cadena a bytes

mensaje30 = 'Hola Mundo'  # Cadena de texto normal
mensaje31 = mensaje30.encode('utf-8')  # Codifica la cadena en bytes usando UTF-8
print(f'{mensaje31} -> Id:{hex(id(mensaje31))} -> {type(mensaje31)}')
mensaje32 = mensaje30.encode('ascii')  # Codifica la cadena en bytes usando ASCII
print(f'{mensaje32} -> Id:{hex(id(mensaje32))} -> {type(mensaje32)}')

# Convertir de Bytes a String
# Las cadenas de bytes se pueden convertir a texto utilizando el método decode() de la clase bytes
mensaje33 = mensaje31.decode('utf-8')  # Decodifica los bytes a una cadena de texto usando UTF-8
print(f'{mensaje33} -> Id:{hex(id(mensaje33))} -> {type(mensaje33)}')
mensaje34 = mensaje32.decode('ascii')  # Decodifica los bytes a una cadena de texto usando ASCII
print(f'{mensaje34} -> Id:{hex(id(mensaje34))} -> {type(mensaje34)}')

