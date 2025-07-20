# Profundizando Listas en Python
# Este archivo define una clase Persona con atributos nombre y apellido,
# listas son mutables

nombres1 = ['Juan', 'Ana', 'Pedro']
nombres2 = 'Laura Maria Gonzalez'.split()

nombres = nombres1 + nombres2
print(nombres)

# Extender una lista con otra lista
nombres1.extend(nombres2)
print(f'Extender de la lista 1 con la lista 2: {nombres1}')

# Lista de numeros
numeros1 = [10, 40, 15, 20, 90]

# Devuelve el indice del primer elemento encontrado
print(f'Indice del primer elemento encontrado: {numeros1.index(15)}')

# invertir el orden de los elementos
numeros1.reverse()
print(f'Lista invertida: {numeros1}')

# Ordenar la lista
numeros1.sort()
print(f'Lista ordenada: {numeros1}')

# Ordenar de forma descendente
numeros1.sort(reverse=True)
print(f'Lista ordenada de forma descendente: {numeros1}')

# Obtener el minimo y maximo de la lista
print(f'Minimo: {min(numeros1)}')
print(f'Maximo: {max(numeros1)}')

# Copiar los elementos de una lista a otra
numeros2 = numeros1.copy()
print(f'Lista original: {numeros1}', hex(id(numeros1)))
print(f'Lista copiada: {numeros2}', hex(id(numeros2)))

numeros2 = list(numeros1)
print(f'Lista original: {numeros1}', hex(id(numeros1)))
print(f'Lista copiada: {numeros2}', hex(id(numeros2)))

# Slicing de listas
numeros2 = numeros1[:]
print(f'Lista original: {numeros1}', hex(id(numeros1)))
print(f'Lista copiada con slicing: {numeros2}', hex(id(numeros2)))

# Multiplicar una lista
lista_multiplicada = 3 * [[1, 2, 3]]
print(f'Lista multiplicada: {lista_multiplicada}')
print(f'ID de la lista multiplicada: {hex(id(lista_multiplicada[0]))}, {hex(id(lista_multiplicada[1]))}, {hex(id(lista_multiplicada[2]))}')

lista_multiplicada[2].append(4)
print(f'Lista multiplicada modificada: {lista_multiplicada}, {hex(id(lista_multiplicada[0]))}, {hex(id(lista_multiplicada[1]))}, {hex(id(lista_multiplicada[2]))})')

# Matrices en python
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f'Matriz: {matriz}')
print(f'Elemento en la fila 1, columna 2: {matriz[1][2]}')

# listas de Listas
lista_de_listas = [[10,14,87,90,71], [4,5,6,7],[9,0,11,15,45,61,70]]
lista_de_listas.sort(key=len)
print(f'Lista de listas ordenada por longitud: {lista_de_listas}')

# Listas de caracteres
nombres1 = ['juan', 'pedro', 'maria']
nombres1=sorted(nombres1)
print(f'Lista de caracteres: {nombres1}')

# Ordenar de forma descendente
nombres1 = ['juan', 'pedro', 'maria']
nombres1=sorted(nombres1,reverse=True)
print(f'Lista de caracteres: {nombres1}')

# Ordenar por longitud de caracteres
nombres1 = ['juan', 'pedro', 'maria del pilar']
nombres1=sorted(nombres1, key=len)
print(f'Lista de caracteres ordenada por longitud: {nombres1}')

# Build-in reversed
nombres1 = reversed(nombres1)
print(f'Lista de caracteres invertida: {list(nombres1)}')

