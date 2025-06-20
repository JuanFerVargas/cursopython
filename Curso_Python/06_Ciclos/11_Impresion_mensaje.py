print('*** Repeticion de un Mensaje ***')

mensaje=input('Proporciona el mensaje a repetir: ')
cantidad=int(input('Proporciona la cantidad de veces a repetir: '))

# Iteramos sobre el rango de repeticiones
for _ in range(cantidad):
    # print(f'{i+1} - {mensaje}')
    print(mensaje)