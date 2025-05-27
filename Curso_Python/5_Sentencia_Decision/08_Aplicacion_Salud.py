print('*** Aplicación de Salud y Fitness***')

# Constantes
META_PASOS_DIARIO=10000
CALORIAS_POR_PASO=0.04  # Valor Aproximado, son KiloCalorias

# Pedimos los valores al usuario
nombre_usuario=input('Cual es tu nombre?: ')
pasos_diarios=int(input('Cuantos pasos has caminado hoy?: '))

# Verificar si el usuario alcanzo la meta de pasos diarios
meta_alcanzada= pasos_diarios>= META_PASOS_DIARIO
meta_alcanzada_txt='Si' if meta_alcanzada else 'No'

# Calculamos las calorias quemadas

calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO

# Mostramos la información

print(f'\nUsuario: {nombre_usuario}')
print(f'Pasos dados hoy: {pasos_diarios}')
print(f'Calorias quemadas: {calorias_quemadas:.1f} kcal')
print(f'Meta de pasos diarios alcanzada: {meta_alcanzada_txt}')
print(f'La meta de pasos diarios es: {META_PASOS_DIARIO} pasos')