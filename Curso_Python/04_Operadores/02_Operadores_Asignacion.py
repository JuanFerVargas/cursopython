# Operadores de Asignación

# Sintaxis operador asignacion

print('*** Operadores de Asignación ***')
numero=5
print(f'Valor de numero= {numero}')

cadena='Saludos desde Python'
print(f'Valor de Cadena= {cadena}')

# Asignación Multiple

numero1,cadena1,florante1=5,'Saludos desde Python',-9.15
print(f'Valor de numero= {numero1}')
print(f'Valor de Cadena= {cadena1}')
print(f'Valor de Florante= {florante1}')

# Asignacion encadenada

a=b=y=10
print(f'Valor de a= {a}')
print(f'Valor de b= {b}')
print(f'Valor de y= {y}')

# Intercambio de valores de una variable, sin utilizar variables temporales
x,y=5,10

# Aplicando el concepto de asignacion multime, intercambiamos valores.

print(f'Valor de x= {x}')
print(f'Valor de y= {y}')
x,y=y,x

print(f'Valor de x= {x}')
print(f'Valor de y= {y}')

# Recibir multiples valores de una entrada del usuario

nombre,apellido=input('Ingrese su nombre y apellido separados por coma: ').split(',')

print(f'Nombre: {nombre.strip()}')
print(f'Apellido: {apellido.strip()}')