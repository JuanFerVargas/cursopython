# Bool contine valores lógicos: True o False
# Booleanos son útiles para tomar decisiones en el código

# Tipo numérico, False si es 0, True si es diferente de 0
print('Conversión de valores a booleano:\n')
valor1=0
resultado1 = bool(valor1)
print(f'El valor {valor1} convertido a booleano es: {resultado1}')

valor2=15
resultado2 = bool(valor2)
print(f'El valor {valor2} convertido a booleano es: {resultado2}\n')

# Tipo cadena, False si está vacía, True si tiene contenido
valor3=''
resultado3 = bool(valor3)
print(f'El valor {valor3} convertido a booleano es: {resultado3}')

valor4='Hola'
resultado4 = bool(valor4)
print(f'El valor {valor4} convertido a booleano es: {resultado4}\n')

# Tipo colecciones, False si está vacío, True si tiene elementos
lista_vacia = []
resultado_lista_vacia = bool(lista_vacia)
print(f'La lista vacía convertida a booleano es: {resultado_lista_vacia}')

lista_con_elementos = [1, 2, 3]
resultado_lista_con_elementos = bool(lista_con_elementos)
print(f'La lista con elementos convertida a booleano es: {resultado_lista_con_elementos}\n')

# Tipo Tupla, False si está vacía, True si tiene elementos
tupla_vacia = ()
resultado_tupla_vacia = bool(tupla_vacia)
print(f'La tupla vacía convertida a booleano es: {resultado_tupla_vacia}')

tupla_con_elementos = (1, 2, 3)
resultado_tupla_con_elementos = bool(tupla_con_elementos)
print(f'La tupla con elementos convertida a booleano es: {resultado_tupla_con_elementos}\n')

# Tipo Diccionario, False si está vacío, True si tiene elementos
diccionario_vacio = {}
resultado_diccionario_vacio = bool(diccionario_vacio)
print(f'El diccionario vacío convertido a booleano es: {resultado_diccionario_vacio}')

diccionario_con_elementos = {'clave': 'valor'}
resultado_diccionario_con_elementos = bool(diccionario_con_elementos)
print(f'El diccionario con elementos convertido a booleano es: {resultado_diccionario_con_elementos}\n')


# Tipo Conjunto, False si está vacío, True si tiene elementos
conjunto_vacio = set()
resultado_conjunto_vacio = bool(conjunto_vacio)
print(f'El conjunto vacío convertido a booleano es: {resultado_conjunto_vacio}')

conjunto_con_elementos = {1, 2, 3}
resultado_conjunto_con_elementos = bool(conjunto_con_elementos)
print(f'El conjunto con elementos convertido a booleano es: {resultado_conjunto_con_elementos}\n')
# Comparaciones booleanas
print('Comparaciones booleanas:\n')

# Ejemplos de comparaciones booleanas
a = 5
b = 10
c = 5

print(f'a = {a}, b = {b}, c = {c}')
print(f'a == b: {a == b}')
print(f'a == c: {a == c}')
print(f'a < b: {a < b}')
print(f'a > b: {a > b}')
print(f'a <= c: {a <= c}')
print(f'a >= c: {a >= c}')

# Operadores lógicos
print('\nOperadores lógicos:\n')
# AND, OR, NOT
print(f'a = {a}, b = {b}, c = {c}')
print(f'a < b AND a == c: {a < b and a == c}')
print(f'a < b OR a == c: {a < b or a == c}')
print(f'NOT (a < b): {not (a < b)}')

# Ejemplo de uso de booleanos en una condición
print('\nUso de booleanos en condiciones:\n')
if a < b:
    print('a es menor que b')
else:
    print('a no es menor que b')

if a == c:
    print('a es igual a c')
else:
    print('a no es igual a c')

# Ejemplo de uso de booleanos en una función
print('\nUso de booleanos en funciones:\n')

def es_mayor_que(a, b):
    return a > b

print(f'es_mayor_que(5, 10): {es_mayor_que(5, 10)}')
print(f'es_mayor_que(10, 5): {es_mayor_que(10, 5)}')

# Ejemplo de uso de booleanos en una lista de comprensión
print('\nUso de booleanos en listas de comprensión:\n')
numeros = [1, 2, 3, 4, 5]
pares = [n for n in numeros if n % 2 == 0]
print(f'Números pares: {pares}')

# Ejemplo de uso de booleanos en un filtro
print('\nUso de booleanos en filtros:\n')
def filtrar_pares(numeros):
    return list(filter(lambda x: x % 2 == 0, numeros))
numeros = [1, 2, 3, 4, 5]
pares = filtrar_pares(numeros)
print(f'Números pares: {pares}')

# Ejemplo de uso de booleanos con ciclo while
print('\nUso de booleanos con ciclo while:\n')
contador = 0
while contador < 5:
    print(f'Contador: {contador}')
    contador += 1

# Ejemplo de uso de booleanos con ciclo for
print('\nUso de booleanos con ciclo for:\n')
for i in range(5):
    print(f'Contador: {i}')
