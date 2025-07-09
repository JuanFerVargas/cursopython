# Profundizando en el tipo float
# El tipo float en Python representa números de punto flotante, que son números reales con decimales. 
# Estos números son útiles para representar cantidades que no son enteras, como medidas, precios, etc.

# Ejemplo de uso del tipo float
precio1 = 19.9999  # Precio de un producto
print(f'Precio1: {precio1:.2f} - Tipo: {type(precio1)}')
precio2 = float('19.9999')  # Convertir un número a float
print(f'Precio2: {precio2:.2f} - Tipo: {type(precio2)}')

# Notacion exponencial (Valores positivos o negativos)
precio3 = 3e10  # 3 * 10^10
print(f'Precio3: {precio3:.2f} - Tipo: {type(precio3)}')
precio4 = 3e-10  # 3 * 10^-10
print(f'Precio4: {precio4:.10f} - Tipo: {type(precio4)}')

# Cualquier calculo tipo float se promieve a float
precio5 = 1 + 2.5  # Suma de un entero y un float
print(f'Precio5: {precio5:.2f} - Tipo: {type(precio5)}')