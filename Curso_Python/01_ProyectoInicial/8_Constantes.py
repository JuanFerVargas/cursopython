# Definicion Constantes
import math

print('*** Constantes en Python ***')

PI = 3.14159
print('El Valor de PI es:', PI)

NOMBRE_BASE_DATOS = 'clientes_db'
print('El nombre de la base de datos es:', NOMBRE_BASE_DATOS)

# No se debe hacer la modificación de una variable constante
NOMBRE_BASE_DATOS = 'listado_clientes_db'
print('No cambiar el valor de una constante:', NOMBRE_BASE_DATOS)

# Usar una constante del lenguaje Python, aunque este no este en mayusculas
print('El valor de math.pi', math.pi)
