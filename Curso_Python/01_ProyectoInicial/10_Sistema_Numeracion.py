# Profundizando Sistemas de Numeración
# Sistemas de Numeración en Python
# Python soporta varios sistemas de numeración para representar números:

# 1. Decimal (Base 10)
a= 10  # Decimal

# 2. Binario (Base 2)
b = 0b1010  # Binario

# 3. Hexadecimal (Base 16)
c = 0xA  # Hexadecimal

# 4. Octal (Base 8)
d = 0o12  # Octal

print(f'a: {a} - Tipo: {type(a)}')
print(f'b: {b} - Tipo: {type(b)}')
print(f'c: {c} - Tipo: {type(c)}')
print(f'd: {d} - Tipo: {type(d)}\n')

# Conversión entre sistemas de numeración
# Convertir un tipo entero, incluyendo base
a=int('23', 10)  # Decimal
b=int('10111', 2)  # Binario
c=int('27', 8)  # Octal
d=int('17', 16)  # Hexadecimal

# Base 5
e = int('43', 5)  # Base 5

print(f'a: {a} - Tipo: {type(a)}')
print(f'b: {b} - Tipo: {type(b)}')
print(f'c: {c} - Tipo: {type(c)}')
print(f'd: {d} - Tipo: {type(d)}')
print(f'e: {e} - Tipo: {type(e)}')


