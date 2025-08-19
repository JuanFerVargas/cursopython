# Profundizando en diccionarios

# Los diccionarios guardan un orden (a partir de Python 3.7) y a diferencia de los sets, pueden contener pares de clave-valor.
diccionario1 = {'Nombre': 'Juan','Apellido': 'Pérez','Edad': 30}
print(diccionario1)

# Los diccionarios son mutables, pero las llaves deben ser inmutables (por ejemplo, cadenas, números o tuplas).
diccionario2 = {(1,2):'valor1'}
print(diccionario2)

# Se agrega una llave con su valor si no se encuentra en su diccionario.
diccionario1['Ciudad'] = 'Madrid'
print(diccionario1)

# No hay valores duplicados en las llaves de un diccionario. (Si ya existe, se reemplaza)
diccionario1['Nombre'] = 'Juan Carlos'
print(diccionario1)

# Recuperar un valor indicando una llave
print(diccionario1['Nombre'])

# Metodo get(), recupera una llave, y si no existe no lanza excepcion
# ademas permite definir un valor por defecto
print(diccionario1.get('Nombre'))
print(diccionario1.get('Nombres', 'No existe'))

# Metodo setdefault(), si modifica el diccionario, ademas se agrega un valor por defecto
nombre = diccionario1.setdefault('Nombres', 'Valor por defecto')
print(nombre)
print(diccionario1)

# Imprimir con pprint
from pprint import pprint as pp
pp(diccionario1,sort_dicts=False)
