# Variable tipo NaN (Not a Number) en Python
# Se utiliza para representar valores numéricos que no son válidos o no están definidos.
import math
from decimal import Decimal

a= float('nan')  # Representa un valor NaN
print(f'Variable tipo NaN: {a}')
print(f'Es NaN (math): {math.isnan(a)}')  # Verifica si es NaN
print(f'Es NaN (Decimal): {Decimal(a).is_nan()}')  # Verifica si es NaN usando Decimal