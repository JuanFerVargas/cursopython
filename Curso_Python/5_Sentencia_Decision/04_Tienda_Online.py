print('*** Tienda en Linea ***')

#Condiciones
MONTO_MINIMO=1000

valor_compra=float(input('Ingrese el valor total de la compra:$ '))
is_member=input('Eres miembro de la tienda? Si/No: ').lower().strip()

if valor_compra>=MONTO_MINIMO and is_member=='si':
    descuento=0.10
    valor_descuento=valor_compra*descuento
    
elif is_member=='si':
    descuento=0.05
    valor_descuento=valor_compra*descuento
else:
    descuento=0
    valor_descuento=0

descuento*=100
valor_final=valor_compra-valor_descuento

if descuento!=0:
    print(f'\nFelicidades, has obtenido un descuento del {descuento:.0f}%')
    print(f'Monto de la compra: ${valor_compra:.2f}')
    print(f'Monto del descuento: ${valor_descuento:.2f}')
    print(f'Monto final de la compra: ${valor_final:.2f}')
else:
    print(f'\nNo obtuviste ningun tipo de descuento \nTe invitamos a hacerte miembro de la tienda')    
    print(f'Monto final de la compra: ${valor_final:.2f}')




