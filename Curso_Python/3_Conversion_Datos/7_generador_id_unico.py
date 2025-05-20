# Sistema Generador ID unico
# Nombre
# Apellido
# Año de Nacimiento
from random import randint

print('*** Sistema Generador ID unico ***')
nombre=input('Digite el nombre: ')
apellido=input('Digite el apellido: ')
anio=input('Digite el Año de nacimiento en formado YYYYY: ')
valor_random=randint(1000,9999)

print(f'Hola {nombre}')
print(f'Resultado ID Único: {(nombre.strip().upper())[0:2]}{(apellido.strip().upper())[0:2]}{anio.strip()[2:4]}{valor_random}')