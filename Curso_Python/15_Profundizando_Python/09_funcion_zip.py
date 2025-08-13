# Funcion Zip
# print(dir(__builtins__))
# print(help(zip))

numeros = [1, 2, 3]
letras = ['a', 'b', 'c', 'd']
indentificadores= 321,322,323,324,325
conjuntos = {99,88,77,66}
resultado = zip(numeros, letras, indentificadores, conjuntos)
print(list(resultado))  # Lista

resultado = zip(numeros, letras, indentificadores, conjuntos)
print(tuple(resultado))  # Tupla
print(type(resultado))  # Tipo de zip

# Iterar en paralelo

for numero, letra, identificador, conjunto in zip(numeros, letras, indentificadores, conjuntos):
    print(f"Numero: {numero}, Letra: {letra}, Identificador: {identificador}, Conjunto: {conjunto}")

nueva_lista = []
for numero, letra, identificador, conjunto in zip(numeros, letras, indentificadores, conjuntos):
    nueva_lista.append(f'{identificador}--{numero}--{letra}--{conjunto}')
print(nueva_lista)

# Desempaquetado de tuplas - Unzip
mezcla = [(1, 'a', 321, 99), (2, 'b', 322, 88), (3, 'c', 323, 77), (4, 'd', 324, 66)]
numeros_unzip, letras_unzip, indentificadores_unzip, conjuntos_unzip = zip(*mezcla)
print(f'Unzip numeros {numeros_unzip}')
print(f'Unzip letras {letras_unzip}')
print(f'Unzip identificadores {indentificadores_unzip}')
print(f'Unzip conjuntos {conjuntos_unzip}')

