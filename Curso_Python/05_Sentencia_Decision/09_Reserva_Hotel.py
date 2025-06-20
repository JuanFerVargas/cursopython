# Reserva Hotel
# Nombre de Cliente
# Dias de estadia en el hotel
# Cuarto con vista al mar?

print('*** Sistema de Reserva de Hotel ***')

# Constantes
ROOMWITH=190.50
ROOMWITHOUT=150.50

# Solicitamos información
nombre_cliente=input('Nombre del Cliente: ')
dias_estadioa=int(input('Dias de estadia: '))
vista_mar= input('Cuarto con vista al mar (Si/No)? ' ).strip().lower()

# Realizamos Calculos
costo_total= dias_estadioa*ROOMWITH if vista_mar=='si' else dias_estadioa*ROOMWITHOUT

# Mostramos informacion
print(f'\n****************** Detalles de la reserva *************************** ')
print(f'Cliente: {nombre_cliente}')
print(f'Dias de estadia: {dias_estadioa}')
print(f'Costo total: {costo_total:.2f}')
print(f'Cuarto con vista al mar: {vista_mar}')