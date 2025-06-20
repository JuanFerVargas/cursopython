print('*** Sistema Empleado ***')
nombre_empleado=input('Nombre del empleado: ')
edad_empleado=int(input('Edad del empleado: '))
salario_empleado=float(input('Salario del empleado:'))
es_jefe_departamento=input('Es jede departamento (Si/No)? ')

# convertimos a tipo Bool la variable
es_jefe_departamento=es_jefe_departamento.lower()=='si'

# Imprimir los valors
print('\nDatos del empleado:')
print('Nombre del empleado:', nombre_empleado)
print('Edad del empleado:', edad_empleado)
print(f'Salario del empleado: {salario_empleado:.2f}')
print('Es jefe de departamento:', es_jefe_departamento)