# unpacking en Python
# El desempaquetado permite extraer valores de una colección (como listas, tuplas, diccionarios) y asignarlos a variables individuales.

valores=1,2,3
print(*valores)  # Desempaquetado de valores
print(type(valores))  # Tipo de la variable valores

# Desempaquetado de una lista
valor1, valor2, valor3 = [1, 2, 3]
print(valor1, valor2, valor3)

# Desempaquetado de una tupla
valor1, _ , valor3 = (1, 2, 3)
print(valor1, valor3)

valor1,valor2, *valor3 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(valor1, valor2, valor3)  # valor3 es una lista con los valores restantes

valor1,valor2, *valor3, valor4, valor5 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(valor1, valor2, valor3,valor4,valor5)  # valor3 es una lista con los valores restantes

def regresar_varios_datos():
    return (1, 2, 3)

valor1, valor2, valor3 = regresar_varios_datos()
print(valor1, valor2, valor3)
print(type(regresar_varios_datos()))  # El tipo de retorno es una tupla

# help(str.partition)  # Ayuda sobre el método partition de la clase str

hora, _, minutos = '17:20'.partition(':')  # Descompone la cadena en una tupla con tres partes
print(type(hora))  # El tipo de hora es una tupla
print(hora,minutos)  # Imprime la tupla resultante del desempaquetado
