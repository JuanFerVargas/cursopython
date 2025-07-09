# Manejo de valores infinitos en Python
# Python permite trabajar con valores infinitos utilizando la clase `float` y las constantes `float('inf')` y `float('-inf')`.
# Estos valores representan infinito positivo y negativo, respectivamente.
# Ejemplo de uso de valores infinitos

import math

# Modulo Decimal para trabajar con decimales y evitar problemas de precisión
from decimal import Decimal


infinito_positivo = float('inf')
infinito_negativo = float('-inf')

print(f'Infinito positivo: {infinito_positivo}')
print(f'Infinito negativo: {infinito_negativo}')

# Comparaciones con valores infinitos
print(f'5 < infinito: {5 < infinito_positivo}')
print(f'5 > infinito: {5 > infinito_negativo}')

# Modulo math para verificar infinito
print(f'Es infinito Positivo: {math.isinf(infinito_positivo)}')
print(f'Es infinito Negativo: {math.isinf(infinito_negativo)}')

nuevo_infinito = math.inf
print(f'Nuevo infinito: {nuevo_infinito}')
print(f'Es infinito: {math.isinf(nuevo_infinito)}')

# Ejemplo de uso del módulo Decimal
infinito = Decimal('Infinity')
print(f'Nuevo infinito: {infinito}')
print(f'Es infinito: {infinito.is_infinite()}')