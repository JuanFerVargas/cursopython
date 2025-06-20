# Generador de Emails
# Nombres
# Apellidos
# Nombre empresa
# Extension Dominio

print('*** Sistema Generador Emails ***')
nombres=input('Ingrese su nombre: ')
apellidos=input('Ingrese su apellido: ')
nombre_empresa=input('Ingrese nombre de Empresa: ')
dominio=input('Ingrese extension del dominio: ')

# tratamiento variables
nombre=nombres.lower().strip().replace(' ','.')
apellido=apellidos.lower().strip().replace(' ','.')
short_name_empresa=nombre_empresa.lower().strip().replace(' ','')
dominio2=dominio.lower()

print(f'Su cuenta de correo es: {nombre}.{apellido}@{short_name_empresa}{dominio2}')

