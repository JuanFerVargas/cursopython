# Desempaquetar listas

from posixpath import sep


numeros=[1,2,3]
print(numeros)
print(*numeros)
print(*numeros, sep=' - ')

# Desempaquetar listas en una función
def sumar(a,b,c):
    print(f'Resultado de la suma: {a + b + c}')

sumar(*numeros)

# Extraer algunas partes de la lista
mi_lista = [1, 2, 3, 4, 5, 6]
a,*b,c,d=mi_lista   # El valor * b captura todos los elementos intermedios
print(a,b,c,d)

# Unir lista
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [lista1, lista2]
print(f'Lista de listas: {lista3}')
lista3 = [*lista1, *lista2]
print(f'Lista de listas con unpacking: {lista3}')

# Unir diccionarios
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5}
dict3 = {**dict1, **dict2}
print(f'Diccionario unido: {dict3}')

# Construir una lista a partir de un string
mi_lista = [*"Hola Mundo"]
print(f'Lista a partir de un string:',*mi_lista)
print(f'Lista a partir de un string sin espacio: ',*mi_lista , sep='')