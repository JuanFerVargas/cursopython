# Generador Email
print('*** Generador de Email ***')
# Nombre Completo
nombre = ' Ubaldo Acosta Soto '
# Nombre limpio sin espacios + en minuscula + reemplazando espacio por (.)
nombre_normalizado = nombre.strip().lower().replace(' ', '.')


nombre_empresa = ' Global Mentoring '
nombre_empresa_normalizado = nombre_empresa.strip().lower().replace(' ', '')
dominio = '.com.mx'
dominio_email_normalizado = f'@{nombre_empresa_normalizado}{dominio}'

print(f'Nombre usuario: {nombre}')
print(f'Nombre usuario normalizado: {nombre_normalizado}\n')

print(f'Nombre empresa: {nombre_empresa}')
print(f'Extensión del dominio: {dominio}')
print(f'Dominio de email normalizado: {dominio_email_normalizado}\n')

print(f'Email final generado: {nombre_normalizado+dominio_email_normalizado}')
