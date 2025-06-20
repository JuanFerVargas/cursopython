print('*** Dibuja Triangulo Simetrico ***')
filas=int(input('Proporciona el numero de Filas: '))

for i in range(filas+1):
    blank_spaces=' '*(filas-i)
    asterisco='*'*(i*2-1)
    print(f'{blank_spaces}{asterisco}')