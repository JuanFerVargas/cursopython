# Conversion de tipos de datos

# Convertir de una cadena a numero

numero_cadena = '10'
numero_entero = int(numero_cadena)
print(f'Valor numerico en cadena: {numero_cadena}')
print(f'Valor numerico entero: {numero_entero}')

# Convertir de cadena a flotante
numero_cadena = '3.14'
numero_flotante = float(numero_cadena)
print(f'Valor numerico flotante: {numero_flotante}')

# Convertir de numero a cadena
numero_entero = 25
numero_cadena = str(numero_entero)
print(f'Valor numerico cadena: {numero_cadena}')

# Convertir a boolean
# Si el valor es 0, cadena vacia, o None, entonces regresa False
# Regresa True, si el valor es distinto de 0, si es distinto de cadena vacia
# y tambien si es distinto de None.

numero_entero = 0
booleano = bool(numero_entero)
print(f'Valor booleano de {numero_entero} es: {booleano}')  # Imprime False


numero_entero = 5
booleano = bool(numero_entero)
print(f'Valor booleano de {numero_entero} es: {booleano}')  # Imprime True


numero_entero = ''  # El largo de la cadena es 0
booleano = bool(numero_entero)
print(f'Valor booleano de {numero_entero} es: {booleano}')  # Imprime False

numero_entero = 'cadena con valor'
booleano = bool(numero_entero)
print(f'Valor booleano de {numero_entero} es: {booleano}')  # Imprime True

numero_entero = None
booleano = bool(numero_entero)
print(f'Valor booleano de {numero_entero} es: {booleano}')  # Imprime False
