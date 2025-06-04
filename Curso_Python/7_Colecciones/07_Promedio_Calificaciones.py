# Aplicaciones para calcular el promedio de calificaciones y sacar el promedio

print('*** Promedio de Calificaciones ***')
count_check=int(input('Proporciona la cantidad de calificaciones a evaluar: '))
calificaciones=[]
sum_calificaciones=0
for calificacion in range(count_check):
    note=float(input(f'calificacion[{calificacion}] = '))
    calificaciones.append(note)
    sum_calificaciones+=note

promedio=sum_calificaciones/count_check
print(f'\nLas Calificaciones proporcionadas son: {calificaciones}')
# sum(lista)
suma_total=sum(calificaciones)
print(f'\nEl promedio de calificaciones es: {promedio:.2f} - {suma_total5}')

