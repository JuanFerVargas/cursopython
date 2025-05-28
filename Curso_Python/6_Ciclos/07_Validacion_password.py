print('*** Validación Password ***')

passsword=input('Ingrese el password: ')
salir=False

# Validar el password
while len(passsword)<6:
    print('El password no cumple con los requisitos. Debe tener al menos 6 caracteres')
    passsword=input('Ingrese un nuevo valor de password: ')

else:
    print(f'El valor de password es valido: ')
